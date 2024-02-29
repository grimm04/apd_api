from rest_framework import serializers
from .models import FrekuensiRTL
from apps.master.opsisdis.frekuensi.models import Frekuensi

class SubRefFrekuensiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Frekuensi
        fields = ['id_meter', 'nama', 'lokasi', 'status']

class FrekuensiRTLSerializers(serializers.ModelSerializer):
    id_meter = serializers.SlugRelatedField(
        queryset=Frekuensi.objects.all(),
        slug_field='id_meter',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_frek = SubRefFrekuensiSerializer(read_only=True, source='id_meter')
    value_1 = serializers.FloatField(default=None, allow_null=True)
    value_2 = serializers.IntegerField(default=None, allow_null=True)
    datum_1 = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S.%f")
    datum_2 = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S.%f")
    statusdata_1 = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    statusdata_2 = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    statusdevice_1 = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    datum_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S.%f")
    datum_updated = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S.%f")
    min_value = serializers.FloatField(default=None, allow_null=True)
    min_datum = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S.%f")
    max_value = serializers.FloatField(default=None, allow_null=True)
    max_datum = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S.%f")

    class Meta:
        model = FrekuensiRTL
        fields = '__all__'