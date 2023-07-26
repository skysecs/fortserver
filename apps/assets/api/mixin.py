from typing import List

from rest_framework.request import Request

from assets.models import Node, Protocol
from assets.utils import get_node_from_request, is_query_node_all_assets
from common.utils import lazyproperty, timeit


class SerializeToTreeNodeMixin:
    request: Request

    @lazyproperty
    def is_sync(self):
        sync_paths = ['/api/v1/perms/users/self/nodes/all-with-assets/tree/']
        for p in sync_paths:
            if p == self.request.path:
                return True
        return False

    @timeit
    def serialize_nodes(self, nodes: List[Node], with_asset_amount=False):
        if with_asset_amount:
            def _name(node: Node):
                return '{} ({})'.format(node.value, node.assets_amount)
        else:
            def _name(node: Node):
                return node.value

        def _open(node):
            if not self.is_sync:
                # 异步加载资产树时，默认展开节点
                return True
            if not node.parent_key:
                return True
            else:
                return False

        data = [
            {
                'id': node.key,
                'name': _name(node),
                'title': _name(node),
                'pId': node.parent_key,
                'isParent': node.assets_amount > 0,
                'open': _open(node),
                'meta': {
                    'data': {
                        "id": node.id,
                        "key": node.key,
                        "value": node.value,
                    },
                    'type': 'node'
                }
            }
            for node in nodes
        ]
        return data

    @lazyproperty
    def support_types(self):
        from assets.const import AllTypes
        return AllTypes.get_types_values(exclude_custom=True)

    def get_icon(self, asset):
        if asset.type in self.support_types:
            return asset.type
        else:
            return 'file'

    @timeit
    def serialize_assets(self, assets, node_key=None, pid=None):
        if node_key is None:
            get_pid = lambda asset: getattr(asset, 'parent_key', '')
        else:
            get_pid = lambda asset: node_key
        sftp_asset_ids = Protocol.objects.filter(name='sftp') \
            .values_list('asset_id', flat=True)
        sftp_asset_ids = list(sftp_asset_ids)
        data = [
            {
                'id': str(asset.id),
                'name': asset.name,
                'title': f'{asset.address}\n{asset.comment}',
                'pId': pid or get_pid(asset),
                'isParent': False,
                'open': False,
                'iconSkin': self.get_icon(asset),
                'chkDisabled': not asset.is_active,
                'meta': {
                    'type': 'asset',
                    'data': {
                        'platform_type': asset.platform.type,
                        'org_name': asset.org_name,
                        'sftp': asset.id in sftp_asset_ids,
                        'name': asset.name,
                        'address': asset.address
                    },
                }
            }
            for asset in assets
        ]
        return data


class NodeFilterMixin:
    request: Request

    @lazyproperty
    def is_query_node_all_assets(self):
        return is_query_node_all_assets(self.request)

    @lazyproperty
    def node(self):
        return get_node_from_request(self.request)
