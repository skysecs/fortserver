# coding: utf-8
#
from celery import shared_task
from django.conf import settings
from django.db import transaction
from django.utils.translation import ugettext_lazy as _

from common.utils import get_logger
from ops.celery.decorator import after_app_ready_start
from ops.celery.utils import (
    create_or_update_celery_periodic_tasks, disable_celery_periodic_task
)
from orgs.models import Organization
from ..utils import LDAPSyncUtil, LDAPServerUtil, LDAPImportUtil

__all__ = ['sync_ldap_user', 'import_ldap_user_periodic', 'import_ldap_user']

logger = get_logger(__file__)


def sync_ldap_user():
    LDAPSyncUtil().perform_sync()


@shared_task(verbose_name=_('Periodic import ldap user'))
def import_ldap_user():
    logger.info("Start import ldap user task")
    util_server = LDAPServerUtil()
    util_import = LDAPImportUtil()
    users = util_server.search()
    if settings.XPACK_ENABLED:
        org_ids = settings.AUTH_LDAP_SYNC_ORG_IDS
        default_org = None
    else:
        # 社区版默认导入Default组织
        org_ids = [Organization.DEFAULT_ID]
        default_org = Organization.default()
    orgs = list(set([Organization.get_instance(org_id, default=default_org) for org_id in org_ids]))
    errors = util_import.perform_import(users, orgs)
    if errors:
        logger.error("Imported LDAP users errors: {}".format(errors))
    else:
        logger.info('Imported {} users successfully'.format(len(users)))


@shared_task(verbose_name=_('Registration periodic import ldap user task'))
@after_app_ready_start
def import_ldap_user_periodic():
    if not settings.AUTH_LDAP:
        return
    task_name = 'import_ldap_user_periodic'
    disable_celery_periodic_task(task_name)
    if not settings.AUTH_LDAP_SYNC_IS_PERIODIC:
        return

    interval = settings.AUTH_LDAP_SYNC_INTERVAL
    if isinstance(interval, int):
        interval = interval * 3600
    else:
        interval = None
    crontab = settings.AUTH_LDAP_SYNC_CRONTAB
    if crontab:
        # 优先使用 crontab
        interval = None
    tasks = {
        task_name: {
            'task': import_ldap_user.name,
            'interval': interval,
            'crontab': crontab,
            'enabled': True,
        }
    }
    create_or_update_celery_periodic_tasks(tasks)
