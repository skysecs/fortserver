from django.utils.translation import gettext_lazy as _

from common.exceptions import JMSException


class SSOAuthClosed(JMSException):
    default_code = 'sso_auth_closed'
    default_detail = _('SSO auth closed')


class WeComCodeInvalid(JMSException):
    default_code = 'wecom_code_invalid'
    default_detail = 'Code invalid, can not get user info'


class WeComBindAlready(JMSException):
    default_code = 'wecom_not_bound'
    default_detail = _('WeCom is already bound')


class WeComNotBound(JMSException):
    default_code = 'wecom_not_bound'
    default_detail = _('WeCom is not bound')


class DingTalkNotBound(JMSException):
    default_code = 'dingtalk_not_bound'
    default_detail = _('DingTalk is not bound')


class FeiShuNotBound(JMSException):
    default_code = 'feishu_not_bound'
    default_detail = _('FeiShu is not bound')


class PasswordInvalid(JMSException):
    default_code = 'passwd_invalid'
    default_detail = _('Your password is invalid')
