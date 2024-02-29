 
from rest_framework import serializers
 
from .models import RefDistrict
from apps.master.wilayah.ref_regency.models import RefRegency
from apps.master.wilayah.ref_regency.serializers import RefRegencyerializer

class RefDistricterializer(serializers.ModelSerializer):
    regency = RefRegencyerializer(source='id_ref_regency')
    class Meta:
        model = RefDistrict
        fields = '__all__'


class CRRefDistrictSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
   
    id_ref_regency = serializers.SlugRelatedField(
        queryset=RefRegency.objects.all(),
        slug_field='id_ref_regency',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    class Meta:
        model = RefDistrict
        fields = '__all__'


class UDRefDistrictSerializers(serializers.ModelSerializer):
    queryset = RefDistrict.objects.all()

    name = serializers.CharField(max_length=100)  
    id_ref_regency = serializers.SlugRelatedField(
        queryset=RefDistrict.objects.all(),
        slug_field='id_ref_regency',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    class Meta:
        model = RefDistrict
        fields = '__all__'
