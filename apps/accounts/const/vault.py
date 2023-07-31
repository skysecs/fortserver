from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = ['VaultTypeChoices']


class VaultTypeChoices(models.TextChoices):
    local = 'local', _('Local Vault')
    hcp = 'hcp', _('HCP Vault')
