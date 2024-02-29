from rest_framework import serializers

from apps.users.models import Users
from apps.master.jaringan.ref_jenis_lokasi.models import RefJenisLokasi
from apps.master.jaringan.ref_lokasi.models import RefLokasi

from apps.master.jaringan.ref_lokasi import serializers as ref_lokasi_serializers
from apps.master.jaringan.ref_jenis_lokasi.serializers import RefJenisLokasierializer


class SubRefLokasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi', 'nama_lokasi']


class RefLokasiSerializer(serializers.ModelSerializer):
    ref_jenis_lokasi = RefJenisLokasierializer(read_only=True, source='id_ref_jenis_lokasi')
    parent_lokasi = ref_lokasi_serializers.IDSRef_LokasiSerializer(read_only=True, source='id_parent_lokasi')
    uid = ref_lokasi_serializers.IDSRef_LokasiSerializer(read_only=True, source='id_uid')
    up3_1 = ref_lokasi_serializers.IDSRef_LokasiSerializer(read_only=True,  source='id_up3_1')
    up3_2 = ref_lokasi_serializers.IDSRef_LokasiSerializer(read_only=True,  source='id_up3_2')
    ulp = ref_lokasi_serializers.IDSRef_LokasiSerializer(read_only=True,  source='id_ulp')
    penyulang = ref_lokasi_serializers.IDSRef_LokasiSerializer(read_only=True,  source='id_penyulang')
    section = ref_lokasi_serializers.IDSRef_LokasiSerializer(read_only=True,  source='id_section')
    segment = ref_lokasi_serializers.IDSRef_LokasiSerializer(read_only=True,  source='id_segment')
    zone = ref_lokasi_serializers.IDSRef_LokasiSerializer(read_only=True,  source='id_zone')
    unit_pembangkit = ref_lokasi_serializers.IDSRef_LokasiSerializer(read_only=True,  source='id_unit_pembangkit')
    pembangkit = ref_lokasi_serializers.IDSRef_LokasiSerializer(read_only=True,  source='id_pembangkit')
    gardu_induk = ref_lokasi_serializers.IDSRef_LokasiSerializer(read_only=True,  source='id_gardu_induk')
    trafo_gi = ref_lokasi_serializers.IDSRef_LokasiSerializer(read_only=True,  source='id_trafo_gi')
    gardu_distribusi = ref_lokasi_serializers.IDSRef_LokasiSerializer(read_only=True,  source='id_gardu_distribusi')
    trafo_gd = ref_lokasi_serializers.IDSRef_LokasiSerializer(read_only=True,  source='id_trafo_gd')
    gardu_hubung = ref_lokasi_serializers.IDSRef_LokasiSerializer(read_only=True, source='id_gardu_hubung') 

    class Meta:
        model = RefLokasi
        fields = '__all__'
        # fields = ['id_ref_lokasi', 'nama_lokasi', 'id_parent_lokasi', 'id_ref_jenis_lokasi']


class BatchRefLokasiSerializer(serializers.ModelSerializer):
    id_ref_lokasi = serializers.IntegerField(default=None)
    id_parent_lokasi = serializers.IntegerField(default=None)
    id_gardu_induk = serializers.IntegerField(default=None)

    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi', 'id_parent_lokasi','id_gardu_induk']
