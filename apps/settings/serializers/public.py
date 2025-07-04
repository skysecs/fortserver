# coding: utf-8
#

from rest_framework import serializers

__all__ = [
    'PublicSettingSerializer', 'PrivateSettingSerializer', 'ServerInfoSerializer'
]


class PublicSettingSerializer(serializers.Serializer):
    XPACK_ENABLED = serializers.BooleanField()
    INTERFACE = serializers.DictField()
    LANGUAGES = serializers.ListField()


class PrivateSettingSerializer(PublicSettingSerializer):
    WINDOWS_SKIP_ALL_MANUAL_PASSWORD = serializers.BooleanField()
    OLD_PASSWORD_HISTORY_LIMIT_COUNT = serializers.IntegerField()
    TICKET_AUTHORIZE_DEFAULT_TIME = serializers.IntegerField()
    TICKET_AUTHORIZE_DEFAULT_TIME_UNIT = serializers.CharField()
    AUTH_LDAP_SYNC_ORG_IDS = serializers.ListField()
    SECURITY_MAX_IDLE_TIME = serializers.IntegerField()
    SECURITY_VIEW_AUTH_NEED_MFA = serializers.BooleanField()
    SECURITY_MFA_AUTH = serializers.IntegerField()
    SECURITY_MFA_VERIFY_TTL = serializers.IntegerField()
    SECURITY_COMMAND_EXECUTION = serializers.BooleanField()
    SECURITY_COMMAND_BLACKLIST = serializers.ListField()
    SECURITY_PASSWORD_EXPIRATION_TIME = serializers.IntegerField()
    SECURITY_EXPIRED_TOKEN_RECORD_KEEP_DAYS = serializers.IntegerField()
    SECURITY_LUNA_REMEMBER_AUTH = serializers.BooleanField()
    SECURITY_WATERMARK_ENABLED = serializers.BooleanField()
    SECURITY_WATERMARK_SESSION_CONTENT = serializers.CharField()
    SECURITY_WATERMARK_CONSOLE_CONTENT = serializers.CharField()
    SECURITY_WATERMARK_COLOR = serializers.CharField()
    SECURITY_WATERMARK_FONT_SIZE = serializers.IntegerField()
    SECURITY_WATERMARK_HEIGHT = serializers.IntegerField()
    SECURITY_WATERMARK_WIDTH = serializers.IntegerField()
    SECURITY_WATERMARK_ROTATE = serializers.IntegerField()
    SESSION_EXPIRE_AT_BROWSER_CLOSE = serializers.BooleanField()
    VIEW_ASSET_ONLINE_SESSION_INFO = serializers.BooleanField()
    PASSWORD_RULE = serializers.DictField()
    SECURITY_SESSION_SHARE = serializers.BooleanField()
    XPACK_LICENSE_IS_VALID = serializers.BooleanField()
    XPACK_LICENSE_EDITION_ULTIMATE = serializers.BooleanField()
    FACE_RECOGNITION_ENABLED = serializers.BooleanField()
    XPACK_LICENSE_INFO = serializers.DictField()
    HELP_DOCUMENT_URL = serializers.CharField()
    HELP_SUPPORT_URL = serializers.CharField()

    AUTH_PASSKEY = serializers.BooleanField()
    AUTH_WECOM = serializers.BooleanField()
    AUTH_DINGTALK = serializers.BooleanField()
    AUTH_FEISHU = serializers.BooleanField()
    AUTH_LARK = serializers.BooleanField()
    AUTH_SLACK = serializers.BooleanField()
    AUTH_TEMP_TOKEN = serializers.BooleanField()

    TERMINAL_RAZOR_ENABLED = serializers.BooleanField()
    TERMINAL_MAGNUS_ENABLED = serializers.BooleanField()
    TERMINAL_KOKO_SSH_ENABLED = serializers.BooleanField()
    TERMINAL_OMNIDB_ENABLED = serializers.BooleanField()

    ANNOUNCEMENT_ENABLED = serializers.BooleanField()
    ANNOUNCEMENT = serializers.DictField()

    TICKETS_ENABLED = serializers.BooleanField()
    TICKETS_DIRECT_APPROVE = serializers.BooleanField()
    CONNECTION_TOKEN_REUSABLE = serializers.BooleanField()
    CACHE_LOGIN_PASSWORD_ENABLED = serializers.BooleanField()
    VAULT_ENABLED = serializers.BooleanField()
    VIRTUAL_APP_ENABLED = serializers.BooleanField()
    CHAT_AI_ENABLED = serializers.BooleanField()
    CHAT_AI_TYPE = serializers.CharField()
    GPT_MODEL = serializers.CharField()
    FILE_UPLOAD_SIZE_LIMIT_MB = serializers.IntegerField()
    FTP_FILE_MAX_STORE = serializers.IntegerField()
    LOKI_LOG_ENABLED = serializers.BooleanField()
    TOOL_USER_ENABLED = serializers.BooleanField()

    DEFAULT_EXPIRED_YEARS = serializers.IntegerField()
    USER_DEFAULT_EXPIRED_DAYS = serializers.IntegerField()
    ASSET_PERMISSION_DEFAULT_EXPIRED_DAYS = serializers.IntegerField()
    PRIVACY_MODE = serializers.BooleanField()
    CHANGE_SECRET_AFTER_SESSION_END = serializers.BooleanField()


class ServerInfoSerializer(serializers.Serializer):
    CURRENT_TIME = serializers.DateTimeField()
