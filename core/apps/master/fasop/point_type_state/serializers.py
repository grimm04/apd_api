from numpy import source
from rest_framework import serializers

from .models import PointTypeState
from apps.master.fasop.point_type.models import PointType


class SubPointTypeSerializer(serializers.ModelSerializer):
    pointtype_name = serializers.CharField(source='name')
    class Meta:
        model = PointType
        fields = ['id_pointtype', 'name', 'jenispoint', 'warna','pointtype_name']


class PointTypeStateSerializers(serializers.ModelSerializer):
    id_pointtype = serializers.SlugRelatedField(
        queryset=PointType.objects.all(),
        slug_field='id_pointtype',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    pointtype = SubPointTypeSerializer(read_only=True, source='id_pointtype')
    name = serializers.CharField(max_length=100)
    status = serializers.IntegerField(default=None)
    valid = serializers.IntegerField(default=None)
    date_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    statekey = serializers.IntegerField(default=None)
    quality_code = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)

    class Meta:
        model = PointTypeState
        fields = '__all__'
