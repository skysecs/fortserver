import base64
import json
from datetime import timedelta

from django.conf import settings
from django.core.cache import cache
from django.db import models
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import PermissionDenied

from accounts.models import VirtualAccount
from assets.const import Protocol
from assets.const.host import GATEWAY_NAME
from authentication.const import ConnectionTokenType
from common.db.fields import EncryptTextField
from common.exceptions import JMSException
from common.utils import lazyproperty, pretty_string, bulk_get, is_uuid
from common.utils.timezone import as_current_tz
from orgs.mixins.models import JMSOrgBaseModel
from orgs.utils import tmp_to_org
from perms.const import ActionChoices
from terminal.models import Applet, VirtualApp


def date_expired_default():
    return timezone.now() + timedelta(seconds=settings.CONNECTION_TOKEN_ONETIME_EXPIRATION)


class ConnectionToken(JMSOrgBaseModel):
    _type = ConnectionTokenType.USER

    value = models.CharField(max_length=64, default='', verbose_name=_("Value"))
    user = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='connection_tokens', verbose_name=_('User')
    )
    asset = models.ForeignKey(
        'assets.Asset', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='connection_tokens', verbose_name=_('Asset'),
    )
    account = models.CharField(max_length=128, verbose_name=_("Account name"))  # 登录账号Name
    input_username = models.CharField(max_length=128, default='', blank=True, verbose_name=_("Input username"))
    input_secret = EncryptTextField(max_length=64, default='', blank=True, verbose_name=_("Input secret"))
    protocol = models.CharField(max_length=16, default=Protocol.ssh, verbose_name=_("Protocol"))
    connect_method = models.CharField(max_length=32, verbose_name=_("Connect method"))
    connect_options = models.JSONField(default=dict, verbose_name=_("Connect options"))
    user_display = models.CharField(max_length=128, default='', verbose_name=_("User display"))
    asset_display = models.CharField(max_length=128, default='', verbose_name=_("Asset display"))
    is_reusable = models.BooleanField(default=False, verbose_name=_("Reusable"))
    date_expired = models.DateTimeField(default=date_expired_default, verbose_name=_("Date expired"))
    from_ticket = models.OneToOneField(
        'tickets.ApplyLoginAssetTicket', related_name='connection_token',
        on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name=_('From ticket')
    )
    face_monitor_token = models.CharField(max_length=128, null=True, blank=True, verbose_name=_("Face monitor token"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active"))

    type = models.CharField(
        max_length=16, choices=ConnectionTokenType.choices,
        default=ConnectionTokenType.USER, verbose_name=_('Type')
    )

    class Meta:
        ordering = ('-date_expired',)
        permissions = [
            ('expire_connectiontoken', _('Can expire connection token')),
            ('reuse_connectiontoken', _('Can reuse connection token')),
        ]
        verbose_name = _('Connection token')

    @classmethod
    def get_typed_connection_token(cls, token_id):
        token = get_object_or_404(cls, id=token_id)

        if token.type == ConnectionTokenType.ADMIN.value:
            token = AdminConnectionToken.objects.get(id=token_id)
        else:
            token = ConnectionToken.objects.get(id=token_id)
        return token

    @property
    def is_expired(self):
        return self.date_expired < timezone.now()

    @property
    def expire_time(self):
        interval = self.date_expired - timezone.now()
        seconds = interval.total_seconds()
        if seconds < 0:
            seconds = 0
        return int(seconds)

    def save(self, *args, **kwargs):
        self.type = self._type
        self.asset_display = pretty_string(self.asset, max_length=128)
        self.user_display = pretty_string(self.user, max_length=128)
        return super().save(*args, **kwargs)

    def expire(self):
        self.date_expired = timezone.now()
        self.save(update_fields=['date_expired'])

    def set_reusable(self, is_reusable):
        if not settings.CONNECTION_TOKEN_REUSABLE:
            return
        self.is_reusable = is_reusable
        if self.is_reusable:
            seconds = settings.CONNECTION_TOKEN_REUSABLE_EXPIRATION
        else:
            seconds = settings.CONNECTION_TOKEN_ONETIME_EXPIRATION

        self.date_expired = self.date_created + timedelta(seconds=seconds)
        self.save(update_fields=['is_reusable', 'date_expired'])

    def renewal(self):
        """ 续期 Token，将来支持用户自定义创建 token 后，续期策略要修改 """
        self.date_expired = date_expired_default()
        self.save()

    @classmethod
    def get_user_permed_account(cls, user, asset, account_alias, protocol):
        from perms.utils import PermAssetDetailUtil
        permed_account = PermAssetDetailUtil(user, asset) \
            .validate_permission(account_alias, protocol)
        return permed_account

    @classmethod
    def get_asset_accounts_by_alias(cls, asset, alias):
        """
        获取资产下的账号
        :param alias: 账号别名
        :return: 账号对象
        """
        if is_uuid(alias):
            kwargs = {'id': alias}
        else:
            kwargs = {'name': alias}

        with tmp_to_org(asset.org_id):
            account = asset.all_valid_accounts.filter(**kwargs).first()
            return account

    def get_permed_account(self):
        return self.get_user_permed_account(self.user, self.asset, self.account, self.protocol)

    @lazyproperty
    def permed_account(self):
        return self.get_permed_account()

    @lazyproperty
    def actions(self):
        return self.permed_account.actions

    @lazyproperty
    def expire_at(self):
        return self.permed_account.date_expired.timestamp()

    def is_valid(self):
        if not self.is_active:
            error = _('Connection token inactive')
            raise PermissionDenied(error)

        if self.is_expired:
            error = _('Connection token expired at: {}').format(as_current_tz(self.date_expired))
            raise PermissionDenied(error)
        if not self.user or not self.user.is_valid:
            error = _('No user or invalid user')
            raise PermissionDenied(error)
        if not self.asset or not self.asset.is_active:
            error = _('No asset or inactive asset')
            raise PermissionDenied(error)
        if not self.account:
            error = _('No account')
            raise PermissionDenied(error)

        if timezone.now() - self.date_created < timedelta(seconds=60):
            return True, None

        permed_account = self.get_permed_account()
        if not permed_account or not permed_account.actions:
            msg = 'user `{}` not has asset `{}` permission for login `{}`'.format(
                self.user, self.asset, self.account
            )
            raise PermissionDenied(msg)

        if self.permed_account.date_expired < timezone.now():
            raise PermissionDenied('Expired')
        return True

    @lazyproperty
    def platform(self):
        return self.asset.platform

    @lazyproperty
    def connect_method_object(self):
        from common.utils import get_request_os
        from fortserver.utils import get_current_request
        from terminal.connect_methods import ConnectMethodUtil

        request = get_current_request()
        os = get_request_os(request) if request else 'windows'
        method = ConnectMethodUtil.get_connect_method(
            self.connect_method, protocol=self.protocol, os=os
        )
        return method

    def get_remote_app_option(self):
        cmdline = {
            'app_name': self.connect_method,
            'user_id': str(self.user.id),
            'asset_id': str(self.asset.id),
            'token_id': str(self.id)
        }
        cmdline_b64 = base64.b64encode(json.dumps(cmdline).encode()).decode()
        app = '||tinker'
        options = {
            'remoteapplicationmode:i': '1',
            'remoteapplicationprogram:s': app,
            'remoteapplicationname:s': app,
            'alternate shell:s': app,
            'remoteapplicationcmdline:s': cmdline_b64,
            'disableconnectionsharing:i': '1',
            'bitmapcachepersistenable:i': '0',  # 图缓存相关设置,便于录像审计
            'bitmapcachesize:i': '1500',
        }
        return options

    def get_virtual_app_option(self):
        method = self.connect_method_object
        if not method or method.get('type') != 'virtual_app' or method.get('disabled', False):
            return None
        virtual_app = VirtualApp.objects.filter(name=method.get('value')).first()
        if not virtual_app:
            return None
        return virtual_app

    def get_applet_option(self):
        method = self.connect_method_object
        if not method or method.get('type') != 'applet' or method.get('disabled', False):
            return None

        applet = Applet.objects.filter(name=method.get('value')).first()
        if not applet:
            return None

        host_account = applet.select_host_account(self.user, self.asset)
        if not host_account:
            raise JMSException({'error': 'No host account available, please check the applet, host and account'})

        host, account, lock_key = bulk_get(host_account, ('host', 'account', 'lock_key'))
        gateway = host.zone.select_gateway() if host.zone else None
        platform = host.platform

        data = {
            'id': lock_key,
            'applet': applet,
            'host': host,
            'gateway': gateway,
            'platform': platform,
            'account': account,
            'remote_app_option': self.get_remote_app_option()
        }
        return data

    @staticmethod
    def release_applet_account(lock_key):
        if lock_key:
            cache.delete(lock_key)
            return True

    def set_ad_domain_if_need(self, account):
        if not self.protocol == 'rdp':
            return
        if account.ds_domain:
            return

        rdp = self.asset.platform.protocols.filter(name='rdp').first()
        if not rdp or not rdp.setting:
            return

        ad_domain = rdp.setting.get('ad_domain')
        if ad_domain:
            # serializer account username 用的是 full_username 所以这么设置
            account.ds_domain = ad_domain

    @lazyproperty
    def account_object(self):
        if not self.asset:
            return None

        if self.account.startswith('@'):
            account = VirtualAccount.get_special_account(
                self.account, self.user, self.asset, input_username=self.input_username,
                input_secret=self.input_secret, from_permed=False
            )
        else:
            account = self.get_asset_accounts_by_alias(self.asset, self.account)
            if not account.secret and self.input_secret:
                account.secret = self.input_secret
            self.set_ad_domain_if_need(account)

        return account

    @lazyproperty
    def zone(self):
        if not self.asset.platform.gateway_enabled:
            return
        if self.asset.platform.name == GATEWAY_NAME:
            return
        zone = self.asset.zone if self.asset.zone else None
        return zone

    @lazyproperty
    def gateway(self):
        if not self.asset or not self.zone:
            return
        return self.asset.gateway

    @lazyproperty
    def command_filter_acls(self):
        from acls.models import CommandFilterACL
        kwargs = {
            'user': self.user,
            'asset': self.asset,
            'account': self.account_object,
        }
        with tmp_to_org(self.asset.org_id):
            acls = CommandFilterACL.filter_queryset(**kwargs).valid()
        return acls


class SuperConnectionToken(ConnectionToken):
    _type = ConnectionTokenType.SUPER

    class Meta:
        proxy = True
        permissions = [
            ('view_superconnectiontokensecret', _('Can view super connection token secret'))
        ]
        verbose_name = _("Super connection token")


class AdminConnectionTokenManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(type=ConnectionTokenType.ADMIN)
        return queryset


class AdminConnectionToken(ConnectionToken):
    _type = ConnectionTokenType.ADMIN

    objects = AdminConnectionTokenManager()

    class Meta:
        proxy = True
        verbose_name = _("Admin connection token")

    @lazyproperty
    def actions(self):
        return ActionChoices.all()

    @lazyproperty
    def expire_at(self):
        return (timezone.now() + timezone.timedelta(days=365)).timestamp()

    def is_valid(self):
        return super().is_valid()

    @classmethod
    def get_user_permed_account(cls, user, asset, account_alias, protocol):
        """
        管理员 token 可以访问所有资产的账号
        """
        account = cls.get_asset_accounts_by_alias(asset, account_alias)
        if not account:
            return None

        account.actions = ActionChoices.all()
        account.date_expired = timezone.now() + timezone.timedelta(days=5)
        return account
