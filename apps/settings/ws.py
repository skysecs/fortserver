# -*- coding: utf-8 -*-
#
import asyncio
import json
from urllib.parse import parse_qs

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.conf import settings
from django.core.cache import cache
from django.utils import translation
from django.utils.translation import gettext_lazy as _

from common.db.utils import close_old_connections
from common.utils import get_logger
from orgs.mixins.ws import OrgMixin
from orgs.models import Organization
from orgs.utils import current_org
from settings.serializers import (
    LDAPHATestConfigSerializer,
    LDAPTestConfigSerializer,
    LDAPTestLoginSerializer
)
from settings.tasks import sync_ldap_user
from settings.utils import (
    LDAPServerUtil, LDAPCacheUtil, LDAPImportUtil, LDAPSyncUtil,
    LDAP_USE_CACHE_FLAGS, LDAPTestUtil
)
from users.models import User
from .const import ImportStatus
from .tools import (
    verbose_ping, verbose_telnet, verbose_nmap,
    verbose_tcpdump, verbose_traceroute
)

logger = get_logger(__name__)

CACHE_KEY_LDAP_TEST_CONFIG_TASK_STATUS = 'CACHE_KEY_LDAP_TEST_CONFIG_TASK_STATUS'
TASK_STATUS_IS_OVER = 'OVER'


class ToolsWebsocket(AsyncJsonWebsocketConsumer, OrgMixin):
    is_closed: bool = False

    @staticmethod
    @sync_to_async
    def get_user_roles(user):
        return [str(i) for i in user.system_roles.values_list('id', flat=True)]

    async def is_superuser(self, user):
        from rbac.builtin import BuiltinRole

        ids = await self.get_user_roles(user)
        return BuiltinRole.system_admin.id in ids

    async def connect(self):
        user = self.scope["user"]
        if user.is_authenticated:
            self.cookie = self.get_cookie()
            self.org = self.get_current_org()
            has_perm = self.has_perms(user, ['rbac.view_systemtools'])
            if await self.is_superuser(user) or (settings.TOOL_USER_ENABLED and has_perm):
                await self.accept()
            else:
                await self.close()
        else:
            await self.close()

    async def send_msg(self, msg=''):
        await self.send_json({'msg': f'{msg}\r\n'})

    async def imitate_ping(self, dest_ips, timeout=3, count=5, psize=64):
        params = {
            'dest_ips': dest_ips, 'timeout': timeout,
            'count': count, 'psize': psize
        }
        logger.info(f'Receive request ping: {params}')
        await verbose_ping(display=self.send_msg, **params)

    async def imitate_telnet(self, dest_ips, dest_port=23, timeout=10):
        params = {
            'dest_ips': dest_ips, 'dest_port': dest_port, 'timeout': timeout,
        }
        logger.info(f'Receive request telnet: {params}')
        await verbose_telnet(display=self.send_msg, **params)

    async def imitate_nmap(self, dest_ips, dest_ports=None, timeout=None):
        params = {
            'dest_ips': dest_ips, 'dest_ports': dest_ports, 'timeout': timeout,
        }
        logger.info(f'Receive request nmap: {params}')
        await verbose_nmap(display=self.send_msg, **params)

    async def imitate_tcpdump(
            self, interfaces=None, src_ips='',
            src_ports='', dest_ips='', dest_ports=''
    ):
        params = {
            'interfaces': interfaces, 'src_ips': src_ips, 'src_ports': src_ports,
            'dest_ips': dest_ips, 'dest_ports': dest_ports
        }
        logger.info(f'Receive request tcpdump: {params}')
        await verbose_tcpdump(display=self.send_msg, **params)

    async def imitate_traceroute(self, dest_ips):
        params = {'dest_ips': dest_ips}
        await verbose_traceroute(display=self.send_msg, **params)

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        data = json.loads(text_data)
        tool_type = data.pop('tool_type', 'Ping')
        try:
            tool_func = getattr(self, f'imitate_{tool_type.lower()}')
            await tool_func(**data)
        except Exception as error:
            await self.send_msg('Exception: %s' % error)
        await self.send_msg()
        await self.close()

    async def close(self, code=None):
        if self.is_closed:
            return
        await super().close(code)
        self.is_closed = True

    async def disconnect(self, code):
        await self.close()
        close_old_connections()


class LdapWebsocket(AsyncJsonWebsocketConsumer):
    category: str

    async def connect(self):
        user = self.scope["user"]
        query = parse_qs(self.scope['query_string'].decode())
        self.category = query.get('category', [User.Source.ldap.value])[0]
        if user.is_authenticated:
            await self.accept()
        else:
            await self.close()

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        data = json.loads(text_data)
        msg_type = data.pop('msg_type', 'testing_config')
        try:
            ok, msg = await asyncio.to_thread(self.run_func, f'run_{msg_type.lower()}', data)
            await self.send_msg(ok, msg)
        except Exception as error:
            await self.send_msg(msg='Exception: %s' % error)

    def run_func(self, func_name, data):
        with translation.override(getattr(self.scope['user'], 'lang', settings.LANGUAGE_CODE)):
            return getattr(self, func_name)(data)

    async def send_msg(self, ok=True, msg=''):
        await self.send_json({'ok': ok, 'msg': f'{msg}'})

    async def disconnect(self, code):
        await self.close()
        close_old_connections()

    def get_ldap_config(self, serializer):
        prefix = 'AUTH_{}_'.format(self.category.upper())

        config = {
            'server_uri': serializer.validated_data.get(f"{prefix}SERVER_URI"),
            'bind_dn': serializer.validated_data.get(f"{prefix}BIND_DN"),
            'password': (serializer.validated_data.get(f"{prefix}BIND_PASSWORD") or
                         getattr(settings, f"{prefix}BIND_PASSWORD")),
            'use_ssl': serializer.validated_data.get(f"{prefix}START_TLS", False),
            'search_ou': serializer.validated_data.get(f"{prefix}SEARCH_OU"),
            'search_filter': serializer.validated_data.get(f"{prefix}SEARCH_FILTER"),
            'attr_map': serializer.validated_data.get(f"{prefix}USER_ATTR_MAP"),
            'auth_ldap': serializer.validated_data.get(f"{prefix.rstrip('_')}", False)
        }

        return config

    @staticmethod
    def task_is_over(task_key):
        return cache.get(task_key) == TASK_STATUS_IS_OVER

    @staticmethod
    def set_task_status_over(task_key, ttl=120):
        cache.set(task_key, TASK_STATUS_IS_OVER, ttl)

    def run_testing_config(self, data):
        if self.category == User.Source.ldap.value:
            serializer = LDAPTestConfigSerializer(data=data)
        else:
            serializer = LDAPHATestConfigSerializer(data=data)
        if not serializer.is_valid():
            self.send_msg(msg=f'error: {str(serializer.errors)}')
        config = self.get_ldap_config(serializer)
        ok, msg = LDAPTestUtil(config).test_config()
        if ok:
            self.set_task_status_over(CACHE_KEY_LDAP_TEST_CONFIG_TASK_STATUS)
        return ok, msg

    def run_testing_login(self, data):
        serializer = LDAPTestLoginSerializer(data=data)
        if not serializer.is_valid():
            self.send_msg(msg=f'error: {str(serializer.errors)}')
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        ok, msg = LDAPTestUtil(category=self.category).test_login(username, password)
        return ok, msg

    def run_sync_user(self, data):
        sync_util = LDAPSyncUtil(category=self.category)
        sync_util.clear_cache()
        sync_ldap_user(category=self.category)
        msg = sync_util.get_task_error_msg()
        ok = False if msg else True
        return ok, msg

    def run_import_user(self, data):
        ok = False
        org_ids = data.get('org_ids')
        username_list = data.get('username_list', [])
        cache_police = data.get('cache_police', True)
        try:
            users = self.get_ldap_users(username_list, cache_police)
            if users is None:
                msg = _('No LDAP user was found')
            else:
                orgs = self.get_orgs(org_ids)
                is_sync_all = '*' in username_list
                new_users, error_msg, disable_users = LDAPImportUtil(
                    self.category, is_sync_all
                ).perform_import(users, orgs)
                ok = True
                success_count = len(users) - len(error_msg)
                msg = _('Total {}, success {}, failure {}').format(
                    len(users), success_count, len(error_msg)
                )
                if disable_users:
                    msg += _(', disabled {}').format(len(disable_users))
                self.set_users_status(users, error_msg)
        except Exception as e:
            msg = str(e)
        return ok, msg

    def set_users_status(self, import_users, errors):
        util = LDAPCacheUtil(category=self.category)
        all_users = util.get_users()
        import_usernames = [u['username'] for u in import_users]
        errors_mapper = {k: v for err in errors for k, v in err.items()}
        for user in all_users:
            username = user['username']
            if username in errors_mapper:
                user['status'] = {'error': errors_mapper[username]}
            elif username in import_usernames:
                user['status'] = ImportStatus.ok
        LDAPCacheUtil(category=self.category).set_users(all_users)

    @staticmethod
    def get_orgs(org_ids):
        if org_ids:
            orgs = list(Organization.objects.filter(id__in=org_ids))
        else:
            orgs = [current_org]
        return orgs

    def get_ldap_users(self, username_list, cache_police):
        if '*' in username_list:
            users = LDAPServerUtil(category=self.category).search()
        elif cache_police in LDAP_USE_CACHE_FLAGS:
            users = LDAPCacheUtil(category=self.category).search(search_users=username_list)
        else:
            users = LDAPServerUtil(category=self.category).search(search_users=username_list)
        return users
