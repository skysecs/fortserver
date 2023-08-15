from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class BasicSettingSerializer(serializers.Serializer):
    PREFIX_TITLE = _('Basic')

    SITE_URL = serializers.URLField(
        required=True, label=_("Site url"),
        help_text=_('Email links or other system callbacks are used to access it, eg: http://dev.fortserver.org:8080')
    )
    USER_GUIDE_URL = serializers.URLField(
        required=False, allow_blank=True, allow_null=True, label=_("User guide url"),
        help_text=_('User first login update profile done redirect to it')
    )
    GLOBAL_ORG_DISPLAY_NAME = serializers.CharField(
        required=False, max_length=1024, allow_blank=True, allow_null=True, label=_("Global organization name"),
        help_text=_('The name of global organization to display')
    )
    HELP_DOCUMENT_URL = serializers.URLField(
        required=False, allow_blank=True, allow_null=True, label=_("Help Docs URL"),
        help_text=_('default: http://docs.fortserver.org')
    )
    HELP_SUPPORT_URL = serializers.URLField(
        required=False, allow_blank=True, allow_null=True, label=_("Help Support URL"),
        help_text=_('default: http://www.fortserver.org/support/')
    )

    @staticmethod
    def validate_SITE_URL(s):
        if not s:
            return 'http://127.0.0.1'
        return s.strip('/')
