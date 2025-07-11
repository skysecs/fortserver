from copy import deepcopy

from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from accounts.automations.methods import platform_automation_methods
from accounts.const import SSHKeyStrategy, SecretStrategy, SecretType, ChangeSecretRecordStatusChoice, \
    ChangeSecretAccountStatus
from accounts.models import BaseAccountQuerySet
from accounts.utils import SecretGenerator, account_secret_task_status
from assets.automations.base.manager import BasePlaybookManager
from assets.const import HostTypes
from common.db.utils import safe_atomic_db_connection
from common.utils import get_logger

logger = get_logger(__name__)


class AccountBasePlaybookManager(BasePlaybookManager):
    template_path = ''

    @property
    def platform_automation_methods(self):
        return platform_automation_methods


class BaseChangeSecretPushManager(AccountBasePlaybookManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.secret_type = self.execution.snapshot.get('secret_type')
        self.secret_strategy = self.execution.snapshot.get(
            'secret_strategy', SecretStrategy.custom
        )
        self.ssh_key_change_strategy = self.execution.snapshot.get(
            'ssh_key_change_strategy', SSHKeyStrategy.set_jms
        )
        self.account_ids = self.execution.snapshot['accounts']
        self.record_map = self.execution.snapshot.get('record_map', {})  # 这个是某个失败的记录重试
        self.name_record_mapper = {}  # 做个映射，方便后面处理

    def gen_account_inventory(self, account, asset, h, path_dir):
        raise NotImplementedError

    def get_ssh_params(self, secret, secret_type):
        kwargs = {}
        if secret_type != SecretType.SSH_KEY:
            return kwargs
        kwargs['strategy'] = self.ssh_key_change_strategy
        kwargs['exclusive'] = 'yes' if kwargs['strategy'] == SSHKeyStrategy.set else 'no'

        if kwargs['strategy'] == SSHKeyStrategy.set_jms:
            kwargs['regexp'] = '.*{}$'.format(secret.split()[2].strip())
        return kwargs

    def get_secret(self, account):
        if self.secret_strategy == SecretStrategy.custom:
            new_secret = self.execution.snapshot['secret']
        else:
            generator = SecretGenerator(
                self.secret_strategy, self.secret_type,
                self.execution.snapshot.get('password_rules')
            )
            new_secret = generator.get_secret()
        return new_secret

    def get_accounts(self, privilege_account) -> BaseAccountQuerySet | None:
        if not privilege_account:
            print('Not privilege account')
            return

        asset = privilege_account.asset
        accounts = asset.all_accounts.all()
        accounts = accounts.filter(id__in=self.account_ids, secret_reset=True)

        if self.secret_type:
            accounts = accounts.filter(secret_type=self.secret_type)

        if settings.CHANGE_AUTH_PLAN_SECURE_MODE_ENABLED:
            accounts = accounts.filter(privileged=False).exclude(
                username__in=['root', 'administrator', privilege_account.username]
            )
        return accounts

    def handle_ssh_secret(self, secret_type, new_secret, path_dir):
        private_key_path = None
        if secret_type == SecretType.SSH_KEY:
            private_key_path = self.generate_private_key_path(new_secret, path_dir)
            new_secret = self.generate_public_key(new_secret)
        return new_secret, private_key_path

    def gen_inventory(self, h, account, new_secret, private_key_path, asset):
        secret_type = account.secret_type
        h['ssh_params'].update(self.get_ssh_params(new_secret, secret_type))
        h['account'] = {
            'name': account.name,
            'username': account.username,
            'full_username': account.full_username,
            'secret_type': secret_type,
            'secret': account.escape_jinja2_syntax(new_secret),
            'private_key_path': private_key_path,
            'become': account.get_ansible_become_auth(),
        }
        if asset.platform.type == 'oracle':
            h['account']['mode'] = 'sysdba' if account.privileged else None
        return h

    def host_callback(self, host, asset=None, account=None, automation=None, path_dir=None, **kwargs):
        host = super().host_callback(
            host, asset=asset, account=account, automation=automation,
            path_dir=path_dir, **kwargs
        )
        if host.get('error'):
            return host

        host['ssh_params'] = {}

        accounts = self.get_accounts(account)
        existing_ids = set(map(str, accounts.values_list('id', flat=True)))
        missing_ids = set(map(str, self.account_ids)) - existing_ids

        for account_id in missing_ids:
            self.clear_account_queue_status(account_id)

        error_msg = _("No pending accounts found")
        if not accounts:
            print(f'{asset}: {error_msg}')
            return []

        if asset.type == HostTypes.WINDOWS:
            accounts = accounts.filter(secret_type=SecretType.PASSWORD)

        inventory_hosts = []
        if asset.type == HostTypes.WINDOWS and self.secret_type == SecretType.SSH_KEY:
            print(f'Windows {asset} does not support ssh key push')
            return inventory_hosts

        for account in accounts:
            h = deepcopy(host)
            h['name'] += '(' + account.username + ')'  # To distinguish different accounts

            account_status = account_secret_task_status.get_status(account.id)
            if account_status == ChangeSecretAccountStatus.PROCESSING:
                h['error'] = f'Account is already being processed, skipping: {account}'
                inventory_hosts.append(h)
                continue

            try:
                h, record = self.gen_account_inventory(account, asset, h, path_dir)
                h['check_conn_after_change'] = record.execution.snapshot.get('check_conn_after_change', True)
                account_secret_task_status.set_status(
                    account.id,
                    ChangeSecretAccountStatus.PROCESSING,
                    metadata={'execution_id': self.execution.id}
                )
            except Exception as e:
                h['error'] = str(e)
                self.clear_account_queue_status(account.id)

            inventory_hosts.append(h)

        return inventory_hosts

    @staticmethod
    def save_record(record):
        record.save(update_fields=['error', 'status', 'date_finished'])

    @staticmethod
    def clear_account_queue_status(account_id):
        account_secret_task_status.clear(account_id)

    def on_host_success(self, host, result):
        record = self.name_record_mapper.get(host)
        if not record:
            return
        record.status = ChangeSecretRecordStatusChoice.success.value
        record.date_finished = timezone.now()

        account = record.account
        if not account:
            print("Account not found, deleted ?")
            return

        account.secret = getattr(record, 'new_secret', account.secret)
        account.date_updated = timezone.now()
        account.date_change_secret = timezone.now()
        account.change_secret_status = ChangeSecretRecordStatusChoice.success

        self.summary['ok_accounts'] += 1
        self.result['ok_accounts'].append(
            {
                "asset": str(account.asset),
                "username": account.username,
            }
        )
        super().on_host_success(host, result)

        with safe_atomic_db_connection():
            account.save(update_fields=['secret', 'date_updated', 'date_change_secret', 'change_secret_status'])
            self.save_record(record)
            self.clear_account_queue_status(account.id)

    def on_host_error(self, host, error, result):
        record = self.name_record_mapper.get(host)
        if not record:
            return
        record.status = ChangeSecretRecordStatusChoice.failed.value
        record.date_finished = timezone.now()
        record.error = error
        account = record.account
        if not account:
            print("Account not found, deleted ?")
            return
        account.date_updated = timezone.now()
        account.date_change_secret = timezone.now()
        account.change_secret_status = ChangeSecretRecordStatusChoice.failed

        self.summary['fail_accounts'] += 1
        self.result['fail_accounts'].append(
            {
                "asset": str(record.asset),
                "username": record.account.username,
            }
        )
        super().on_host_error(host, error, result)

        with safe_atomic_db_connection():
            account.save(update_fields=['change_secret_status', 'date_change_secret', 'date_updated'])
            self.save_record(record)
            self.clear_account_queue_status(account.id)
