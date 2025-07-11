# -*- coding: utf-8 -*-
#

from django.db.models import F
from django.utils.timezone import get_current_timezone
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from accounts.models import Account
from assets.const import Category, AllTypes
from assets.models import Node, Asset, Platform
from assets.serializers.asset.common import AssetProtocolsPermsSerializer
from common.serializers import ResourceLabelsMixin
from common.serializers.fields import ObjectRelatedField, LabeledChoiceField
from orgs.mixins.serializers import OrgResourceModelSerializerMixin
from perms.serializers.permission import ActionChoicesField

__all__ = [
    'NodePermedSerializer', 'AssetPermedSerializer',
    'AssetPermedDetailSerializer', 'AccountsPermedSerializer'
]


class AssetPermedSerializer(OrgResourceModelSerializerMixin, ResourceLabelsMixin):
    """ 被授权资产的数据结构 """
    platform = ObjectRelatedField(required=False, queryset=Platform.objects, label=_('Platform'))
    category = LabeledChoiceField(choices=Category.choices, read_only=True, label=_('Category'))
    type = LabeledChoiceField(choices=AllTypes.choices(), read_only=True, label=_('Type'))
    zone = ObjectRelatedField(required=False, read_only=True, label=_('Zone'))

    class Meta:
        model = Asset
        only_fields = [
            'id', 'name', 'address', 'zone', 'platform',
            'comment', 'org_id', 'is_active', 'date_verified',
            'created_by', 'date_created', 'connectivity', 'nodes', 'labels'
        ]
        fields = only_fields + ['category', 'type'] + ['org_name']
        read_only_fields = fields

    @classmethod
    def setup_eager_loading(cls, queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.prefetch_related('zone', 'nodes') \
            .prefetch_related('platform') \
            .annotate(category=F("platform__category")) \
            .annotate(type=F("platform__type"))
        return queryset


class NodePermedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = [
            'id', 'name', 'key', 'value', 'full_value',
            'org_id', "assets_amount"
        ]
        read_only_fields = fields


class AccountsPermedSerializer(serializers.ModelSerializer):
    actions = ActionChoicesField(read_only=True)
    username = serializers.CharField(source='full_username', read_only=True)
    date_expired = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = [
            'id', 'alias', 'name', 'username', 'has_username',
            'has_secret', 'secret_type', 'actions', 'date_expired'
        ]
        read_only_fields = fields

    def get_date_expired(self, obj):
        dt = obj.date_expired
        if dt:
            dt = dt.astimezone(get_current_timezone())
            formatted = dt.strftime('%Y/%m/%d %H:%M:%S %z')
            return formatted
        else:
            return None


class AssetPermedDetailSerializer(AssetPermedSerializer):
    # 前面特意加了 permed，避免返回的是资产本身的
    permed_protocols = AssetProtocolsPermsSerializer(many=True, required=False, label=_('Protocols'))
    permed_accounts = AccountsPermedSerializer(label=_("Accounts"), required=False, many=True)

    class Meta(AssetPermedSerializer.Meta):
        fields = AssetPermedSerializer.Meta.fields + ['spec_info', 'permed_protocols', 'permed_accounts']
        read_only_fields = fields
