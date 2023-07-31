from contextlib import contextmanager

from django.db import connections

from common.utils import get_logger

logger = get_logger(__file__)


def get_object_if_need(model, pk):
    if not isinstance(pk, model):
        try:
            return model.objects.get(id=pk)
        except model.DoesNotExist as e:
            logger.error(f'DoesNotExist: <{model.__name__}:{pk}> not exist')
            raise e
    return pk


def get_objects_if_need(model, pks):
    if not pks:
        return pks
    if not isinstance(pks[0], model):
        objs = list(model.objects.filter(id__in=pks))
        if len(objs) != len(pks):
            pks = set(pks)
            exists_pks = {o.id for o in objs}
            not_found_pks = ','.join(pks - exists_pks)
            logger.error(f'DoesNotExist: <{model.__name__}: {not_found_pks}>')
        return objs
    return pks


def get_objects(model, pks):
    if not pks:
        return pks

    objs = list(model.objects.filter(id__in=pks))
    if len(objs) != len(pks):
        pks = set(pks)
        exists_pks = {o.id for o in objs}
        not_found_pks = pks - exists_pks
        logger.error(f'DoesNotExist: <{model.__name__}: {not_found_pks}>')
    return objs


# 复制 django.db.close_old_connections, 因为它没有导出，ide 提示有问题
def close_old_connections():
    for conn in connections.all():
        conn.close_if_unusable_or_obsolete()


@contextmanager
def safe_db_connection():
    close_old_connections()
    yield
    close_old_connections()
