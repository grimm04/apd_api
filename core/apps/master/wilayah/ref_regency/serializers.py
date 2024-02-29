from rest_framework import serializers

from apps.master.wilayah.ref_province.models import RefProvince
from apps.master.wilayah.ref_province.serializers import RefProvincSerializers
from .models import RefRegency


class RefRegencyerializer(serializers.ModelSerializer):
    province = RefProvincSerializers(source='id_ref_province')
    class Meta:
        model = RefRegency
        fields = '__all__'


class CRRefRegencySerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
   
    id_ref_province = serializers.SlugRelatedField(
        queryset=RefProvince.objects.all(),
        slug_field='id_ref_province',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    class Meta:
        model = RefRegency
        fields = '__all__'


class UDRefRegencySerializers(serializers.ModelSerializer):
    queryset = RefRegency.objects.all()

    name = serializers.CharField(max_length=100)  
    id_ref_province = serializers.SlugRelatedField(
        queryset=RefRegency.objects.all(),
        slug_field='id_ref_province',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    class Meta:
        model = RefRegency
        fields = '__all__'
