import base64
import json
import os
import urllib.parse

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework import status, serializers
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from accounts.const import AliasAccount
from acls.notifications import AssetLoginReminderMsg
from common.api import JMSModelViewSet
from common.exceptions import JMSException
from common.utils import random_string, get_logger, get_request_ip
from common.utils.django import get_request_os
from common.utils.http import is_true, is_false
from orgs.mixins.api import RootOrgViewMixin
from orgs.utils import tmp_to_org
from perms.models import ActionChoices
from terminal.connect_methods import NativeClient, ConnectMethodUtil
from terminal.models import EndpointRule, Endpoint
from users.const import FileNameConflictResolution
from users.models import Preference
from ..models import ConnectionToken, date_expired_default
from ..serializers import (
    ConnectionTokenSerializer, ConnectionTokenSecretSerializer,
    SuperConnectionTokenSerializer, ConnectTokenAppletOptionSerializer,
    ConnectionTokenReusableSerializer,
)

__all__ = ['ConnectionTokenViewSet', 'SuperConnectionTokenViewSet']
logger = get_logger(__name__)


class RDPFileClientProtocolURLMixin:
    request: Request
    get_serializer: callable

    def get_rdp_file_info(self, token: ConnectionToken):
        rdp_options = {
            'full address:s': '',
            'username:s': '',
            'use multimon:i': '0',
            'session bpp:i': '32',
            'audiomode:i': '0',
            'disable wallpaper:i': '0',
            'disable full window drag:i': '0',
            'disable menu anims:i': '0',
            'disable themes:i': '0',
            'alternate shell:s': '',
            'shell working directory:s': '',
            'authentication level:i': '2',
            'connect to console:i': '0',
            'disable cursor setting:i': '0',
            'allow font smoothing:i': '1',
            'allow desktop composition:i': '1',
            'redirectprinters:i': '0',
            'prompt for credentials on client:i': '0',
            'autoreconnection enabled:i': '1',
            'bookmarktype:i': '3',
            'use redirection server name:i': '0',
            'smart sizing:i': '1',
        }
        # 设置多屏显示
        multi_mon = is_true(self.request.query_params.get('multi_mon'))
        if multi_mon:
            rdp_options['use multimon:i'] = '1'

        # 设置多屏显示
        multi_mon = is_true(self.request.query_params.get('multi_mon'))
        if multi_mon:
            rdp_options['use multimon:i'] = '1'

        # 设置磁盘挂载
        drives_redirect = is_true(self.request.query_params.get('drives_redirect'))
        if drives_redirect:
            if ActionChoices.contains(token.actions, ActionChoices.transfer()):
                rdp_options['drivestoredirect:s'] = '*'

        # 设置全屏
        full_screen = is_true(self.request.query_params.get('full_screen'))
        rdp_options['screen mode id:i'] = '2' if full_screen else '1'

        # 设置 RDP Server 地址
        endpoint = self.get_smart_endpoint(protocol='rdp', asset=token.asset)
        rdp_options['full address:s'] = f'{endpoint.host}:{endpoint.rdp_port}'

        # 设置用户名
        rdp_options['username:s'] = '{}|{}'.format(token.user.username, str(token.id))
        # rdp_options['domain:s'] = token.account_ad_domain

        # 设置宽高
        height = self.request.query_params.get('height')
        width = self.request.query_params.get('width')
        if width and height:
            rdp_options['desktopwidth:i'] = width
            rdp_options['desktopheight:i'] = height
            rdp_options['winposstr:s'] = f'0,1,0,0,{width},{height}'
            rdp_options['dynamic resolution:i'] = '0'

        # 设置其他选项
        rdp_options['session bpp:i'] = os.getenv('fortserver_COLOR_DEPTH', '32')
        rdp_options['audiomode:i'] = self.parse_env_bool('fortserver_DISABLE_AUDIO', 'false', '2', '0')

        # 设置远程应用, 不是 Mstsc
        if token.connect_method != NativeClient.mstsc:
            remote_app_options = token.get_remote_app_option()
            rdp_options.update(remote_app_options)

        rdp = token.asset.platform.protocols.filter(name='rdp').first()
        if rdp and rdp.setting.get('console'):
            rdp_options['administrative session:i'] = '1'

        # 文件名
        name = token.asset.name
        prefix_name = f'{token.user.username}-{name}'
        filename = self.get_connect_filename(prefix_name)

        content = ''
        for k, v in rdp_options.items():
            content += f'{k}:{v}\n'

        return filename, content

    @staticmethod
    def escape_name(name):
        name = name.replace('/', '_')
        name = name.replace('\\', '_')
        name = name.replace('.', '_')
        name = urllib.parse.quote(name)
        return name

    def get_connect_filename(self, prefix_name):
        filename = f'{prefix_name}-fortserver'
        filename = self.escape_name(filename)
        return filename

    @staticmethod
    def parse_env_bool(env_key, env_default, true_value, false_value):
        return true_value if is_true(os.getenv(env_key, env_default)) else false_value

    def get_client_protocol_data(self, token: ConnectionToken):
        _os = get_request_os(self.request)

        connect_method_name = token.connect_method
        connect_method_dict = ConnectMethodUtil.get_connect_method(
            token.connect_method, token.protocol, _os
        )
        asset = token.asset
        if connect_method_dict is None:
            raise ValueError('Connect method not support: {}'.format(connect_method_name))

        account = token.account or token.input_username
        datetime = timezone.localtime(timezone.now()).strftime('%Y-%m-%d_%H:%M:%S')
        name = account + '@' + str(asset) + '[' + datetime + ']'
        data = {
            'version': 2,
            'id': str(token.id),  # 兼容老的，未来几个版本删掉
            'value': token.value,  # 兼容老的，未来几个版本删掉
            'name': self.escape_name(name),
            'protocol': token.protocol,
            'token': {
                'id': str(token.id),
                'value': token.value,
            },
            'file': {},
            'command': ''
        }

        if connect_method_name == NativeClient.mstsc or connect_method_dict['type'] == 'applet':
            filename, content = self.get_rdp_file_info(token)
            data.update({
                'protocol': 'rdp',
                'file': {
                    'name': filename,
                    'content': content,
                }
            })
        else:
            endpoint = self.get_smart_endpoint(
                protocol=connect_method_dict['endpoint_protocol'],
                asset=asset
            )
            data.update({
                'asset': {
                    'id': str(asset.id),
                    'category': asset.category,
                    'type': asset.type,
                    'name': asset.name,
                    'address': asset.address,
                    'info': {
                        **asset.spec_info,
                    }
                },
                'endpoint': {
                    'host': endpoint.host,
                    'port': endpoint.get_port(token.asset, token.protocol),
                }
            })
        return data

    def get_smart_endpoint(self, protocol, asset=None):
        endpoint = Endpoint.match_by_instance_label(asset, protocol)
        if not endpoint:
            target_ip = asset.get_target_ip() if asset else ''
            endpoint = EndpointRule.match_endpoint(
                target_instance=asset, target_ip=target_ip,
                protocol=protocol, request=self.request
            )
        return endpoint


class ExtraActionApiMixin(RDPFileClientProtocolURLMixin):
    request: Request
    get_object: callable
    get_serializer: callable
    perform_create: callable
    validate_exchange_token: callable

    @action(methods=['POST', 'GET'], detail=True, url_path='rdp-file')
    def get_rdp_file(self, *args, **kwargs):
        token = self.get_object()
        token.is_valid()
        filename, content = self.get_rdp_file_info(token)
        filename = '{}.rdp'.format(filename)
        response = HttpResponse(content, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'%s' % filename
        return response

    @action(methods=['POST', 'GET'], detail=True, url_path='client-url')
    def get_client_protocol_url(self, *args, **kwargs):
        token = self.get_object()
        token.is_valid()
        try:
            protocol_data = self.get_client_protocol_data(token)
        except ValueError as e:
            return Response(data={'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        protocol_data = json.dumps(protocol_data).encode()
        protocol_data = base64.b64encode(protocol_data).decode()
        data = {
            'url': 'jms://{}'.format(protocol_data)
        }
        return Response(data=data)

    @action(methods=['PATCH'], detail=True)
    def expire(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.expire()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['PATCH'], detail=True, url_path='reuse')
    def reuse(self, request, *args, **kwargs):
        instance = self.get_object()
        if not settings.CONNECTION_TOKEN_REUSABLE:
            error = _('Reusable connection token is not allowed, global setting not enabled')
            raise serializers.ValidationError(error)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        is_reusable = serializer.validated_data.get('is_reusable', False)
        instance.set_reusable(is_reusable)
        return Response(data=serializer.data)

    @action(methods=['POST'], detail=False)
    def exchange(self, request, *args, **kwargs):
        pk = request.data.get('id', None) or request.data.get('pk', None)
        # 只能兑换自己使用的 Token
        instance = get_object_or_404(ConnectionToken, pk=pk, user=request.user)
        instance.id = None
        self.validate_exchange_token(instance)
        instance.date_expired = date_expired_default()
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ConnectionTokenViewSet(ExtraActionApiMixin, RootOrgViewMixin, JMSModelViewSet):
    filterset_fields = (
        'user_display', 'asset_display'
    )
    search_fields = filterset_fields
    serializer_classes = {
        'default': ConnectionTokenSerializer,
        'reuse': ConnectionTokenReusableSerializer,
    }
    http_method_names = ['get', 'post', 'patch', 'head', 'options', 'trace']
    rbac_perms = {
        'list': 'authentication.view_connectiontoken',
        'retrieve': 'authentication.view_connectiontoken',
        'create': 'authentication.add_connectiontoken',
        'exchange': 'authentication.add_connectiontoken',
        'reuse': 'authentication.reuse_connectiontoken',
        'expire': 'authentication.expire_connectiontoken',
        'get_rdp_file': 'authentication.add_connectiontoken',
        'get_client_protocol_url': 'authentication.add_connectiontoken',
    }

    def get_queryset(self):
        queryset = ConnectionToken.objects \
            .filter(user=self.request.user) \
            .filter(date_expired__gt=timezone.now())
        return queryset

    def get_user(self, serializer):
        return self.request.user

    def perform_create(self, serializer):
        self.validate_serializer(serializer)
        return super().perform_create(serializer)

    def _insert_connect_options(self, data, user):
        connect_options = data.pop('connect_options', {})
        default_name_opts = {
            'file_name_conflict_resolution': FileNameConflictResolution.REPLACE,
            'terminal_theme_name': 'Default',
        }
        preferences_query = Preference.objects.filter(
            user=user, category='koko', name__in=default_name_opts.keys()
        ).values_list('name', 'value')
        preferences = dict(preferences_query)
        for name in default_name_opts.keys():
            value = preferences.get(name, default_name_opts[name])
            connect_options[name] = value
        data['connect_options'] = connect_options

    def validate_serializer(self, serializer):
        data = serializer.validated_data
        user = self.get_user(serializer)
        self._insert_connect_options(data, user)
        asset = data.get('asset')
        account_name = data.get('account')
        _data = self._validate(user, asset, account_name)
        data.update(_data)
        return serializer

    def validate_exchange_token(self, token):
        user = token.user
        asset = token.asset
        account_name = token.account
        _data = self._validate(user, asset, account_name)
        for k, v in _data.items():
            setattr(token, k, v)
        return token

    def _validate(self, user, asset, account_name):
        data = dict()
        data['org_id'] = asset.org_id
        data['user'] = user
        data['value'] = random_string(16)

        if account_name == AliasAccount.ANON and asset.category not in ['web', 'custom']:
            raise ValidationError(_('Anonymous account is not supported for this asset'))

        account = self._validate_perm(user, asset, account_name)
        if account.has_secret:
            data['input_secret'] = ''

        if account.username != AliasAccount.INPUT:
            data['input_username'] = ''
        ticket = self._validate_acl(user, asset, account)
        if ticket:
            data['from_ticket'] = ticket
            data['is_active'] = False
        return data

    @staticmethod
    def _validate_perm(user, asset, account_name):
        from perms.utils.account import PermAccountUtil
        account = PermAccountUtil().validate_permission(user, asset, account_name)
        if not account or not account.actions:
            msg = _('Account not found')
            raise JMSException(code='perm_account_invalid', detail=msg)
        if account.date_expired < timezone.now():
            msg = _('Permission expired')
            raise JMSException(code='perm_expired', detail=msg)
        return account

    @staticmethod
    def _record_operate_log(acl, asset):
        from audits.handler import create_or_update_operate_log
        with tmp_to_org(asset.org_id):
            after = {str(_('Assets')): str(asset)}
            object_name = acl._meta.object_name
            resource_type = acl._meta.verbose_name
            create_or_update_operate_log(
                acl.action, resource_type, resource=acl,
                after=after, object_name=object_name
            )

    def _validate_acl(self, user, asset, account):
        from acls.models import LoginAssetACL
        acls = LoginAssetACL.filter_queryset(user=user, asset=asset, account=account)
        ip = get_request_ip(self.request)
        acl = LoginAssetACL.get_match_rule_acls(user, ip, acls)
        if not acl:
            return
        if acl.is_action(acl.ActionChoices.accept):
            self._record_operate_log(acl, asset)
            return
        if acl.is_action(acl.ActionChoices.reject):
            self._record_operate_log(acl, asset)
            msg = _('ACL action is reject: {}({})'.format(acl.name, acl.id))
            raise JMSException(code='acl_reject', detail=msg)
        if acl.is_action(acl.ActionChoices.review):
            if not self.request.query_params.get('create_ticket'):
                msg = _('ACL action is review')
                raise JMSException(code='acl_review', detail=msg)
            self._record_operate_log(acl, asset)
            ticket = LoginAssetACL.create_login_asset_review_ticket(
                user=user, asset=asset, account_username=account.username,
                assignees=acl.reviewers.all(), org_id=asset.org_id
            )
            return ticket
        if acl.is_action(acl.ActionChoices.notice):
            reviewers = acl.reviewers.all()
            if not reviewers:
                return
            account_username = account.username
            self._record_operate_log(acl, asset)
            for reviewer in reviewers:
                AssetLoginReminderMsg(reviewer, asset, user, account_username).publish_async()


class SuperConnectionTokenViewSet(ConnectionTokenViewSet):
    serializer_classes = {
        'default': SuperConnectionTokenSerializer,
        'get_secret_detail': ConnectionTokenSecretSerializer,
    }
    rbac_perms = {
        'create': 'authentication.add_superconnectiontoken',
        'renewal': 'authentication.add_superconnectiontoken',
        'get_secret_detail': 'authentication.view_superconnectiontokensecret',
        'get_applet_info': 'authentication.view_superconnectiontoken',
        'release_applet_account': 'authentication.view_superconnectiontoken',
    }

    def get_queryset(self):
        return ConnectionToken.objects.all()

    def get_user(self, serializer):
        return serializer.validated_data.get('user')

    @action(methods=['PATCH'], detail=False)
    def renewal(self, request, *args, **kwargs):
        from common.utils.timezone import as_current_tz

        token_id = request.data.get('id') or ''
        token = get_object_or_404(ConnectionToken, pk=token_id)
        date_expired = as_current_tz(token.date_expired)
        if token.is_expired:
            raise PermissionDenied('Token is expired at: {}'.format(date_expired))
        token.renewal()
        data = {
            'ok': True,
            'msg': f'Token is renewed, date expired: {date_expired}'
        }
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False, url_path='secret')
    def get_secret_detail(self, request, *args, **kwargs):
        """ 非常重要的 api, 在逻辑层再判断一下 rbac 权限, 双重保险 """
        rbac_perm = 'authentication.view_superconnectiontokensecret'
        if not request.user.has_perm(rbac_perm):
            raise PermissionDenied('Not allow to view secret')

        token_id = request.data.get('id') or ''
        token = get_object_or_404(ConnectionToken, pk=token_id)
        token.is_valid()
        serializer = self.get_serializer(instance=token)

        expire_now = request.data.get('expire_now', None)
        asset_type = token.asset.type
        # 设置默认值
        if expire_now is None:
            # TODO 暂时特殊处理 k8s 不过期
            if asset_type in ['k8s', 'kubernetes']:
                expire_now = False
            else:
                expire_now = not settings.CONNECTION_TOKEN_REUSABLE

        if is_false(expire_now):
            logger.debug('Api specified, now expire now')
        elif token.is_reusable and settings.CONNECTION_TOKEN_REUSABLE:
            logger.debug('Token is reusable, not expire now')
        else:
            token.expire()

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False, url_path='applet-option')
    def get_applet_info(self, *args, **kwargs):
        token_id = self.request.data.get('id')
        token = get_object_or_404(ConnectionToken, pk=token_id)
        if token.is_expired:
            return Response({'error': 'Token expired'}, status=status.HTTP_400_BAD_REQUEST)
        data = token.get_applet_option()
        serializer = ConnectTokenAppletOptionSerializer(data)
        return Response(serializer.data)

    @action(methods=['DELETE', 'POST'], detail=False, url_path='applet-account/release')
    def release_applet_account(self, *args, **kwargs):
        account_id = self.request.data.get('id')
        released = ConnectionToken.release_applet_account(account_id)

        if released:
            logger.debug('Release applet account success: {}'.format(account_id))
            return Response({'msg': 'released'})
        else:
            logger.error('Release applet account error: {}'.format(account_id))
            return Response({'error': 'not found or expired'}, status=400)
