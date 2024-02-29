from rest_framework import serializers

from .models import FASOPMASTER
from apps.master.fasop.point_type.models import PointType
from apps.master.jaringan.ref_lokasi.models import RefLokasi


class SubPointTypeSerializer(serializers.ModelSerializer):
    nama_jenis = serializers.CharField(source='name')
    class Meta:
        model = PointType
        fields = ['id_pointtype', 'name', 'jenispoint', 'warna','nama_jenis']

class SubRefLokasiSerializer(serializers.ModelSerializer):

    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi', 'nama_lokasi', 'kode_lokasi']


class FASOPMASTERSerializers(serializers.ModelSerializer):
    path3text = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
    path3 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
    status = serializers.IntegerField()
    faktor = serializers.CharField(max_length=18, allow_blank=True, allow_null=True) 
    send_telegram = serializers.IntegerField()
    kinerja = serializers.IntegerField()
    id_pointtype = serializers.SlugRelatedField(
        queryset=PointType.objects.all(),
        slug_field='id_pointtype',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    pointtype = SubPointTypeSerializer(read_only=True, source='id_pointtype')
    id_ref_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_lokasi = SubRefLokasiSerializer(read_only=True, source='id_ref_lokasi')

    class Meta:
        model = FASOPMASTER
        fields = '__all__'
