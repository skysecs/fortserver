from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

__all__ = [
    'SSOSettingSerializer',
]


class SSOSettingSerializer(serializers.Serializer):
    PREFIX_TITLE = _('SSO')

    AUTH_SSO = serializers.BooleanField(
        required=False, label=_('Enable SSO auth'),
        help_text=_("Other service can using SSO token login to fortserver without password")
    )
    AUTH_SSO_AUTHKEY_TTL = serializers.IntegerField(
        required=False, label=_('SSO auth key TTL'), help_text=_("Unit: second"),
        min_value=60, max_value=60 * 30
    )
