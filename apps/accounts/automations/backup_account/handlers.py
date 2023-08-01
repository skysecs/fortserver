import os
import time
from collections import defaultdict, OrderedDict

from django.conf import settings
from openpyxl import Workbook
from rest_framework import serializers

from accounts.notifications import AccountBackupExecutionTaskMsg
from accounts.serializers import AccountSecretSerializer
from assets.const import AllTypes
from common.utils.file import encrypt_and_compress_zip_file
from common.utils.timezone import local_now_display
from users.models import User

PATH = os.path.join(os.path.dirname(settings.BASE_DIR), 'tmp')


class BaseAccountHandler:
    @classmethod
    def unpack_data(cls, serializer_data, data=None):
        if data is None:
            data = {}
        for k, v in serializer_data.items():
            if isinstance(v, OrderedDict):
                cls.unpack_data(v, data)
            else:
                data[k] = v
        return data

    @classmethod
    def get_header_fields(cls, serializer: serializers.Serializer):
        try:
            backup_fields = getattr(serializer, 'Meta').fields_backup
        except AttributeError:
            backup_fields = serializer.fields.keys()
        header_fields = {}
        for field in backup_fields:
            v = serializer.fields[field]
            if isinstance(v, serializers.Serializer):
                _fields = cls.get_header_fields(v)
                header_fields.update(_fields)
            else:
                header_fields[field] = str(v.label)
        return header_fields

    @classmethod
    def create_row(cls, data, header_fields):
        data = cls.unpack_data(data)
        row_dict = {}
        for field, header_name in header_fields.items():
            row_dict[header_name] = str(data.get(field, field))
        return row_dict

    @classmethod
    def add_rows(cls, data, header_fields, sheet):
        data_map = defaultdict(list)
        for i in data:
            row = cls.create_row(i, header_fields)
            if sheet not in data_map:
                data_map[sheet].append(list(row.keys()))
            data_map[sheet].append(list(row.values()))
        return data_map


class AssetAccountHandler(BaseAccountHandler):
    @staticmethod
    def get_filename(plan_name):
        filename = os.path.join(
            PATH, f'{plan_name}-{local_now_display()}-{time.time()}.xlsx'
        )
        return filename

    @classmethod
    def create_data_map(cls, accounts):
        data_map = defaultdict(list)

        if not accounts.exists():
            return data_map

        type_dict = {}
        for i in AllTypes.grouped_choices_to_objs():
            for j in i['children']:
                type_dict[j['value']] = j['display_name']

        header_fields = cls.get_header_fields(AccountSecretSerializer(accounts.first()))
        account_type_map = defaultdict(list)
        for account in accounts:
            account_type_map[account.type].append(account)

        data_map = {}
        for tp, _accounts in account_type_map.items():
            sheet_name = type_dict.get(tp, tp)
            data = AccountSecretSerializer(_accounts, many=True).data
            data_map.update(cls.add_rows(data, header_fields, sheet_name))

        print('\n\033[33m- 共备份 {} 条账号\033[0m'.format(accounts.count()))
        return data_map


class AccountBackupHandler:
    def __init__(self, execution):
        self.execution = execution
        self.plan_name = self.execution.plan.name
        self.is_frozen = False  # 任务状态冻结标志

    def create_excel(self):
        print(
            '\n'
            '\033[32m>>> 正在生成资产或应用相关备份信息文件\033[0m'
            ''
        )
        # Print task start date
        time_start = time.time()
        files = []
        accounts = self.execution.backup_accounts
        data_map = AssetAccountHandler.create_data_map(accounts)
        if not data_map:
            return files

        filename = AssetAccountHandler.get_filename(self.plan_name)

        wb = Workbook(filename)
        for sheet, data in data_map.items():
            ws = wb.create_sheet(str(sheet))
            for row in data:
                ws.append(row)
        wb.save(filename)
        files.append(filename)
        timedelta = round((time.time() - time_start), 2)
        print('步骤完成: 用时 {}s'.format(timedelta))
        return files

    def send_backup_mail(self, files, recipients):
        if not files:
            return
        recipients = User.objects.filter(id__in=list(recipients))
        print(
            '\n'
            '\033[32m>>> 发送备份邮件\033[0m'
            ''
        )
        plan_name = self.plan_name
        for user in recipients:
            if not user.secret_key:
                attachment_list = []
            else:
                password = user.secret_key.encode('utf8')
                attachment = os.path.join(PATH, f'{plan_name}-{local_now_display()}-{time.time()}.zip')
                encrypt_and_compress_zip_file(attachment, password, files)
                attachment_list = [attachment, ]
            AccountBackupExecutionTaskMsg(plan_name, user).publish(attachment_list)
            print('邮件已发送至{}({})'.format(user, user.email))
        for file in files:
            os.remove(file)

    def step_perform_task_update(self, is_success, reason):
        self.execution.reason = reason[:1024]
        self.execution.is_success = is_success
        self.execution.save()
        print('已完成对任务状态的更新')

    def step_finished(self, is_success):
        if is_success:
            print('任务执行成功')
        else:
            print('任务执行失败')

    def _run(self):
        is_success = False
        error = '-'
        try:
            recipients = self.execution.plan_snapshot.get('recipients')
            if not recipients:
                print(
                    '\n'
                    '\033[32m>>> 该备份任务未分配收件人\033[0m'
                    ''
                )
            else:
                files = self.create_excel()
                self.send_backup_mail(files, recipients)
        except Exception as e:
            self.is_frozen = True
            print('任务执行被异常中断')
            print('下面打印发生异常的 Traceback 信息 : ')
            print(e)
            error = str(e)
        else:
            is_success = True
        finally:
            reason = error
            self.step_perform_task_update(is_success, reason)
            self.step_finished(is_success)

    def run(self):
        print('任务开始: {}'.format(local_now_display()))
        time_start = time.time()
        try:
            self._run()
        except Exception as e:
            print('任务运行出现异常')
            print('下面显示异常 Traceback 信息: ')
            print(e)
        finally:
            print('\n任务结束: {}'.format(local_now_display()))
            timedelta = round((time.time() - time_start), 2)
            print('用时: {}'.format(timedelta))
