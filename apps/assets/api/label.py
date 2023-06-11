# ~*~ coding: utf-8 ~*~
# Copyright (C) 2014-2018 Beijing DuiZhan Technology Co.,Ltd. All Rights Reserved.
#
# Licensed under the GNU General Public License v2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.gnu.org/licenses/gpl-2.0.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.db.models import Count

from common.utils import get_logger
from orgs.mixins.api import OrgBulkModelViewSet
from ..models import Label
from .. import serializers


logger = get_logger(__file__)
__all__ = ['LabelViewSet']


class LabelViewSet(OrgBulkModelViewSet):
    model = Label
    filterset_fields = ("name", "value")
    search_fields = filterset_fields
    serializer_class = serializers.LabelSerializer

    def list(self, request, *args, **kwargs):
        if request.query_params.get("distinct"):
            self.serializer_class = serializers.LabelDistinctSerializer
            self.queryset = self.queryset.values("name").distinct()
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        self.queryset = Label.objects.annotate(asset_count=Count("assets"))
        return self.queryset
