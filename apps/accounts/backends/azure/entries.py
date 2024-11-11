import sys
from abc import ABC

from common.db.utils import Encryptor
from common.utils import lazyproperty

current_module = sys.modules[__name__]

__all__ = ['build_entry']


class BaseEntry(ABC):

    def __init__(self, instance):
        self.instance = instance

    @lazyproperty
    def full_path(self):
        return self.path_spec

    @property
    def path_spec(self):
        raise NotImplementedError

    def to_internal_data(self):
        secret = getattr(self.instance, '_secret', None)
        if secret is not None:
            secret = Encryptor(secret).encrypt()
        return secret

    @staticmethod
    def to_external_data(secret):
        if secret is not None:
            secret = Encryptor(secret).decrypt()
        return secret


class AccountEntry(BaseEntry):

    @property
    def path_spec(self):
        # 长度 0-127
        account_id = str(self.instance.id)[:18]
        path = f'assets-{self.instance.asset_id}-accounts-{account_id}'
        return path


class AccountTemplateEntry(BaseEntry):

    @property
    def path_spec(self):
        path = f'account-templates-{self.instance.id}'
        return path


class HistoricalAccountEntry(BaseEntry):

    @property
    def path_spec(self):
        path = f'accounts-{self.instance.instance.id}-histories-{self.instance.history_id}'
        return path


def build_entry(instance) -> BaseEntry:
    class_name = instance.__class__.__name__
    entry_class_name = f'{class_name}Entry'
    entry_class = getattr(current_module, entry_class_name, None)
    if not entry_class:
        raise Exception(f'Entry class {entry_class_name} is not found')
    return entry_class(instance)
