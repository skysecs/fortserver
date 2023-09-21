from django.conf import settings
from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from assets.models import Asset
from common.permissions import IsValidUser
from ops.const import Types
from ops.models import Job, JobExecution
from ops.serializers.job import JobSerializer, JobExecutionSerializer

__all__ = [
    'JobViewSet', 'JobExecutionViewSet', 'JobRunVariableHelpAPIView',
    'JobAssetDetail', 'JobExecutionTaskDetail', 'UsernameHintsAPI'
]

from ops.tasks import run_ops_job_execution
from ops.variables import JMS_JOB_VARIABLE_HELP
from orgs.mixins.api import OrgBulkModelViewSet
from orgs.utils import tmp_to_org, get_current_org
from accounts.models import Account
from perms.models import PermNode
from perms.utils import UserPermAssetUtil


def set_task_to_serializer_data(serializer, task_id):
    data = getattr(serializer, "_data", {})
    data["task_id"] = task_id
    setattr(serializer, "_data", data)


def merge_nodes_and_assets(nodes, assets, user):
    if nodes:
        perm_util = UserPermAssetUtil(user=user)
        for node_id in nodes:
            if node_id == PermNode.FAVORITE_NODE_KEY:
                node_assets = perm_util.get_favorite_assets()
            elif node_id == PermNode.UNGROUPED_NODE_KEY:
                node_assets = perm_util.get_ungroup_assets()
            else:
                node, node_assets = perm_util.get_node_all_assets(node_id)
            assets.extend(node_assets.exclude(id__in=[asset.id for asset in assets]))
    return assets


class JobViewSet(OrgBulkModelViewSet):
    serializer_class = JobSerializer
    search_fields = ('name', 'comment')
    model = Job

    def check_permissions(self, request):
        if not settings.SECURITY_COMMAND_EXECUTION:
            return self.permission_denied(request, "Command execution disabled")
        return super().check_permissions(request)

    def allow_bulk_destroy(self, qs, filtered):
        return True

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(creator=self.request.user)
        if self.action != 'retrieve':
            return queryset.filter(instant=False)
        return queryset

    def perform_create(self, serializer):
        run_after_save = serializer.validated_data.pop('run_after_save', False)
        node_ids = serializer.validated_data.pop('nodes', [])
        assets = serializer.validated_data.__getitem__('assets')
        assets = merge_nodes_and_assets(node_ids, assets, self.request.user)
        serializer.validated_data.__setitem__('assets', assets)
        instance = serializer.save()
        if instance.instant or run_after_save:
            self.run_job(instance, serializer)

    def perform_update(self, serializer):
        run_after_save = serializer.validated_data.pop('run_after_save', False)
        instance = serializer.save()
        if run_after_save:
            self.run_job(instance, serializer)

    def run_job(self, job, serializer):
        execution = job.create_execution()
        execution.creator = self.request.user
        execution.save()

        set_task_to_serializer_data(serializer, execution.id)
        run_ops_job_execution.apply_async((str(execution.id),), task_id=str(execution.id))


class JobExecutionViewSet(OrgBulkModelViewSet):
    serializer_class = JobExecutionSerializer
    http_method_names = ('get', 'post', 'head', 'options',)
    model = JobExecution
    search_fields = ('material',)
    filterset_fields = ['status', 'job_id']

    @staticmethod
    def start_deploy(instance, serializer):
        task = run_ops_job_execution.apply_async((str(instance.id),), task_id=str(instance.id))

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.job_version = instance.job.version
        instance.material = instance.job.material
        instance.job_type = Types[instance.job.type].value
        instance.creator = self.request.user
        instance.save()

        set_task_to_serializer_data(serializer, instance.id)
        run_ops_job_execution.apply_async((str(instance.id),), task_id=str(instance.id))

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(creator=self.request.user)
        return queryset


class JobAssetDetail(APIView):
    rbac_perms = {
        'get': ['ops.view_jobexecution'],
    }

    def get(self, request, **kwargs):
        execution_id = request.query_params.get('execution_id', '')
        execution = get_object_or_404(JobExecution, id=execution_id)
        return Response(data=execution.assent_result_detail)


class JobExecutionTaskDetail(APIView):
    rbac_perms = {
        'GET': ['ops.view_jobexecution'],
    }

    def get(self, request, **kwargs):
        org = get_current_org()
        task_id = str(kwargs.get('task_id'))

        with tmp_to_org(org):
            execution = get_object_or_404(JobExecution, task_id=task_id)

        return Response(data={
            'status': execution.status,
            'is_finished': execution.is_finished,
            'is_success': execution.is_success,
            'time_cost': execution.time_cost,
            'job_id': execution.job.id,
        })


class JobRunVariableHelpAPIView(APIView):
    permission_classes = [IsValidUser]

    def get(self, request, **kwargs):
        return Response(data=JMS_JOB_VARIABLE_HELP)


class UsernameHintsAPI(APIView):
    permission_classes = [IsValidUser]

    def post(self, request, **kwargs):
        node_ids = request.data.get('nodes', None)
        asset_ids = request.data.get('assets', [])
        query = request.data.get('query', None)

        assets = list(Asset.objects.filter(id__in=asset_ids).all())

        assets = merge_nodes_and_assets(node_ids, assets, request.user)

        top_accounts = Account.objects \
                           .exclude(username__startswith='jms_') \
                           .exclude(username__startswith='js_') \
                           .filter(username__icontains=query) \
                           .filter(asset__in=assets) \
                           .values('username') \
                           .annotate(total=Count('username')) \
                           .order_by('total', '-username')[:10]
        return Response(data=top_accounts)
