from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from common.serializers.fields import EncryptedField

__all__ = ['WeComSettingSerializer']


class WeComSettingSerializer(serializers.Serializer):
    PREFIX_TITLE = _('WeCom')

    WECOM_CORPID = serializers.CharField(max_length=256, required=True, label='Corporation ID')
    WECOM_AGENTID = serializers.CharField(max_length=256, required=True, label='App Agent ID')
    WECOM_SECRET = EncryptedField(max_length=256, required=False, label='App Secret')
    AUTH_WECOM = serializers.BooleanField(default=False, label=_('WeCom'))
