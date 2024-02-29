 
from rest_framework import serializers
from .models import FrekuensiTH
from apps.master.opsisdis.frekuensi.models import Frekuensi
from apps.master.jaringan.ref_lokasi.models import RefLokasi

# class SubRefLokasiSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = RefLokasi
#         fields = ['id_ref_lokasi', 'nama_lokasi', 'kode_lokasi']

class SubRefFrekuensiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Frekuensi
        fields = ['id_meter', 'nama', 'lokasi', 'status']

class FrekuensiTHSerializers(serializers.ModelSerializer):
    id_meter = serializers.SlugRelatedField(
        queryset=Frekuensi.objects.all(),
        slug_field='id_meter',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_frek = SubRefFrekuensiSerializer(read_only=True, source='id_meter')
    datum = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    range_nilai = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    lokasi = serializers.CharField(max_length=100, allow_null=True, allow_blank=True, required=False)
    jumlah = serializers.IntegerField(default=None, allow_null=True)
    datum_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    # id_ref_lokasi = serializers.SlugRelatedField(
    #     queryset=RefLokasi.objects.all(),
    #     slug_field='id_ref_lokasi',
    #     allow_null=True,
    #     required=False,
    #     style={'base_template': 'input.html'}
    # )
    # ref_lokasi = SubRefLokasiSerializer(read_only=True, source='id_ref_lokasi')

    class Meta:
        model = FrekuensiTH
        fields = '__all__'