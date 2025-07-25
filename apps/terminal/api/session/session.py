# -*- coding: utf-8 -*-
#
import os
import tarfile

from django.conf import settings
from django.core.cache import cache
from django.core.files.storage import default_storage
from django.db.models import F
from django.http import FileResponse
from django.shortcuts import get_object_or_404, reverse
from django.utils.encoding import escape_uri_path
from django.utils.translation import gettext_noop, gettext as _
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework import viewsets, views
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from audits.const import ActionChoices
from audits.utils import record_operate_log_and_activity_log
from common.api import AsyncApiMixin
from common.const.http import GET, POST
from common.drf.filters import BaseFilterSet
from common.drf.filters import DatetimeRangeFilterBackend
from common.drf.renders import PassthroughRenderer
from common.permissions import IsServiceAccount
from common.storage.replay import ReplayStorageHandler, SessionPartReplayStorageHandler
from common.utils import data_to_json, is_uuid, i18n_fmt
from common.utils import get_logger, get_object_or_none
from orgs.mixins.api import OrgBulkModelViewSet
from orgs.utils import tmp_to_root_org, tmp_to_org
from rbac.permissions import RBACPermission
from terminal import serializers
from terminal.const import TerminalType
from terminal.models import Session
from terminal.permissions import IsSessionAssignee
from terminal.session_lifecycle import lifecycle_events_map, reasons_map
from terminal.utils import is_session_approver
from users.models import User

__all__ = [
    'SessionViewSet', 'SessionReplayViewSet',
    'SessionJoinValidateAPI', 'MySessionAPIView'
]

logger = get_logger(__name__)

REPLAY_OP = gettext_noop('User %s %s session %s replay')


class MySessionAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.SessionSerializer

    def get_queryset(self):
        user = self.request.user
        qs = Session.objects.filter(user_id=user.id)
        return qs


class SessionFilterSet(BaseFilterSet):
    terminal = filters.CharFilter(method='filter_terminal')

    class Meta:
        model = Session
        fields = [
            "user", "user_id", "asset", "asset_id", "account", "remote_addr",
            "protocol", "is_finished", 'login_from', 'terminal'
        ]

    @staticmethod
    def filter_terminal(queryset, name, value):
        if is_uuid(value):
            return queryset.filter(terminal__id=value)
        else:
            return queryset.filter(terminal__name=value)


class SessionViewSet(OrgBulkModelViewSet):
    model = Session
    serializer_classes = {
        'default': serializers.SessionSerializer,
        'display': serializers.SessionDisplaySerializer,
        'lifecycle_log': serializers.SessionLifecycleLogSerializer,
    }
    search_fields = [
        "user", "asset", "account", "remote_addr",
        "protocol", "is_finished", 'login_from',
    ]
    filterset_class = SessionFilterSet
    date_range_filter_fields = [
        ('date_start', ('date_from', 'date_to'))
    ]
    extra_filter_backends = [DatetimeRangeFilterBackend]
    rbac_perms = {
        'download': ['terminal.download_sessionreplay'],
    }
    permission_classes = [RBACPermission]

    def get_permissions(self):
        if self.action == 'retrieve':
            self.permission_classes = [RBACPermission | IsSessionAssignee]
        return super().get_permissions()

    @staticmethod
    def prepare_offline_file(session, local_path):
        replay_path = default_storage.path(local_path)
        current_dir = os.getcwd()
        dir_path = os.path.dirname(replay_path)
        replay_filename = os.path.basename(replay_path)
        meta_filename = '{}.json'.format(session.id)
        offline_filename = '{}.tar'.format(session.id)
        os.chdir(dir_path)

        with open(meta_filename, 'wt') as f:
            serializer = serializers.SessionDisplaySerializer(session)
            data = data_to_json(serializer.data)
            f.write(data)

        with tarfile.open(offline_filename, 'w') as f:
            f.add(replay_filename)
            f.add(meta_filename)
        file = open(offline_filename, 'rb')
        os.chdir(current_dir)
        return file

    @action(methods=[GET], detail=True, renderer_classes=(PassthroughRenderer,), url_path='replay/download',
            url_name='replay-download')
    def download(self, request, *args, **kwargs):
        session = self.get_object()
        storage = ReplayStorageHandler(session)
        local_path, url = storage.get_file_path_url()
        if local_path is None:
            # url => error message
            return Response({'error': url}, status=404)

        # 如果获取的录像文件类型是 .replay.json 则使用 part 的方式下载
        if url.endswith('.replay.json'):
            # part 的方式录像存储, 通过 part_storage 的方式下载
            part_storage = SessionPartReplayStorageHandler(session)
            file = part_storage.prepare_offline_tar_file()
        else:
            file = self.prepare_offline_file(session, local_path)
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        # 这里要注意哦，网上查到的方法都是response['Content-Disposition']='attachment;filename="filename.py"',
        # 但是如果文件名是英文名没问题，如果文件名包含中文，下载下来的文件名会被改为url中的path。
        filename = escape_uri_path('{}.tar'.format(session.id))
        disposition = "attachment; filename*=UTF-8''{}".format(filename)
        response["Content-Disposition"] = disposition

        detail = i18n_fmt(
            REPLAY_OP, self.request.user, _('Download'), str(session)
        )
        record_operate_log_and_activity_log(
            [session.asset_id], ActionChoices.download, detail, Session,
            resource_display=f'{session.asset}', resource_type=_('Session replay')
        )
        return response

    @action(methods=[GET], detail=False, permission_classes=[IsAuthenticated], url_path='online-info', )
    def online_info(self, request, *args, **kwargs):
        if not settings.VIEW_ASSET_ONLINE_SESSION_INFO:
            return self.permission_denied(request, "view asset online session info disabled")
        asset = self.request.query_params.get('asset_id')
        account = self.request.query_params.get('account')
        if asset is None or account is None:
            return Response({'count': None})

        queryset = Session.objects.filter(is_finished=False) \
            .filter(asset_id=asset) \
            .filter(protocol='rdp')  # 当前只统计 rdp 协议的会话
        if '(' in account and ')' in account:
            queryset = queryset.filter(account=account)
        else:
            queryset = queryset.filter(account__endswith='({})'.format(account))
        count = queryset.count()
        return Response({'count': count})

    @action(methods=[POST], detail=True, permission_classes=[IsServiceAccount], url_path='lifecycle_log',
            url_name='lifecycle_log')
    def lifecycle_log(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        event = validated_data.pop('event', None)
        event_class = lifecycle_events_map.get(event, None)
        if not event_class:
            return Response({'msg': f'event_name {event} invalid'}, status=400)
        session = self.get_object()
        reason = validated_data.pop('reason', None)
        reason = reasons_map.get(reason, reason)
        event_obj = event_class(session, reason, **validated_data)
        activity_log = event_obj.create_activity_log()
        return Response({'msg': 'ok', 'id': activity_log.id})

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.method in ('GET',):
            queryset = queryset.prefetch_related('terminal').annotate(terminal_display=F('terminal__name'))
        elif self.request.method in ('PATCH',):
            # postgres reports an error for statements that use select_for_update for out join
            # so we need to use select_for_update only for have not prefetch_related and annotate
            queryset = queryset.select_for_update()
        return queryset

    def perform_create(self, serializer):
        if hasattr(self.request.user, 'terminal'):
            serializer.validated_data["terminal"] = self.request.user.terminal
        return super().perform_create(serializer)


class SessionReplayViewSet(AsyncApiMixin, viewsets.ViewSet):
    serializer_class = serializers.ReplaySerializer
    view_replay_cache_key = "SESSION_REPLAY_VIEW_{}"
    session = None
    rbac_perms = {
        'create': 'terminal.upload_sessionreplay',
        'retrieve': 'terminal.view_sessionreplay',
    }

    def create(self, request, *args, **kwargs):
        session_id = kwargs.get('pk')
        session = get_object_or_404(Session, id=session_id)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            file = serializer.validated_data['file']
            # 兼容旧版本 API 未指定 version 为 2 的情况
            version = serializer.validated_data.get('version', 2)
            name, err = session.save_replay_to_storage_with_version(file, version)
            if not name:
                msg = "Failed save replay `{}`: {}".format(session_id, err)
                logger.error(msg)
                return Response({'msg': str(err)}, status=400)
            url = default_storage.url(name)
            return Response({'url': url}, status=201)
        else:
            msg = 'Upload data invalid: {}'.format(serializer.errors)
            logger.error(msg)
            return Response({'msg': serializer.errors}, status=401)

    @staticmethod
    def get_replay_data(session, url):
        all_guacamole_types = (
            TerminalType.lion, TerminalType.guacamole,
            TerminalType.razor, TerminalType.xrdp
        )

        if url.endswith('.cast.gz'):
            tp = 'asciicast'
        elif url.endswith('.replay.mp4'):
            tp = 'mp4'
        elif url.endswith('replay.json'):
            # 新版本将返回元数据信息
            tp = 'parts'
        elif (getattr(session.terminal, 'type', None) in all_guacamole_types) or \
                (session.protocol in ('rdp', 'vnc')):
            tp = 'guacamole'
        else:
            tp = 'json'

        download_url = reverse('api-terminal:session-replay-download', kwargs={'pk': session.id})
        data = {
            'type': tp, 'src': url,
            'user': session.user, 'asset': session.asset,
            'account': session.account,
            'date_start': session.date_start,
            'date_end': session.date_end,
            'download_url': download_url,
        }
        return data

    def is_need_async(self):
        if self.action != 'retrieve':
            return False
        return True

    def async_callback(self, *args, **kwargs):
        session_id = kwargs.get('pk')
        session = get_object_or_404(Session, id=session_id)
        detail = i18n_fmt(
            REPLAY_OP, self.request.user, _('View'), str(session)
        )
        key = self.view_replay_cache_key.format(session_id)
        if cache.get(key):
            return
        record_operate_log_and_activity_log(
            [session.asset_id], ActionChoices.view, detail, Session,
            resource_display=f'{session.asset}', resource_type=_('Session replay')
        )
        cache.set(key, 1, 10)

    def retrieve(self, request, *args, **kwargs):
        session_id = kwargs.get('pk')
        session = get_object_or_404(Session, id=session_id)
        part_filename = request.query_params.get('part_filename')
        if part_filename:
            storage = SessionPartReplayStorageHandler(session)
            local_path, url = storage.get_part_file_path_url(part_filename)
        else:
            storage = ReplayStorageHandler(session)
            local_path, url = storage.get_file_path_url()

        if local_path is None:
            # url => error message
            return Response({"error": url}, status=404)
        data = self.get_replay_data(session, url)
        return Response(data)


class SessionJoinValidateAPI(views.APIView):
    """
    监控用
    """
    serializer_class = serializers.SessionJoinValidateSerializer
    rbac_perms = {
        'POST': 'terminal.validate_sessionactionperm'
    }

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            msg = str(serializer.errors)
            return Response({'ok': False, 'msg': msg}, status=401)
        user_id = serializer.validated_data['user_id']
        session_id = serializer.validated_data['session_id']

        with tmp_to_root_org():
            session = get_object_or_none(Session, pk=session_id)
        if not session:
            msg = _('Session does not exist: {}'.format(session_id))
            return Response({'ok': False, 'msg': msg}, status=401)
        if not session.can_join:
            msg = _('Session is finished or the protocol not supported')
            return Response({'ok': False, 'msg': msg}, status=401)

        user = get_object_or_none(User, pk=user_id)
        if not user:
            msg = _('User does not exist: {}'.format(user_id))
            return Response({'ok': False, 'msg': msg}, status=401)

        with tmp_to_org(session.org):
            if is_session_approver(session_id, user_id):
                return Response({'ok': True, 'msg': ''}, status=200)

            if not user.has_perm('terminal.monitor_session'):
                msg = _('User does not have permission')
                return Response({'ok': False, 'msg': msg}, status=401)

        return Response({'ok': True, 'msg': ''}, status=200)
