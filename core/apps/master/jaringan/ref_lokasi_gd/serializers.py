from rest_framework import serializers

from apps.master.jaringan.ref_lokasi.models import RefLokasi

from .models import RefLokasiGD

from apps.master.jaringan.ref_lokasi import serializers as ref_lokasi_serializers
from apps.master.jaringan.ref_jenis_lokasi.serializers import RefJenisLokasierializer
from apps.master.jaringan.ref_jenis_pembangkit.serializers import RefJenisPembangkiterializer

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


class RefLokasChildierializer(serializers.ModelSerializer): 
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
        fields =  '__all__'


class RefLokasiGDSerializer(serializers.ModelSerializer):
    id_ref_lokasi = RefLokasiSerializer(read_only=True)
    id_ref_lokasi_child = RefLokasChildierializer(required=False)

    class Meta:
        model = RefLokasiGD
        fields = '__all__'


class CRRefLokasiGDSerializers(serializers.ModelSerializer):
    id_ref_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        style={'base_template': 'input.html'}
    )
    id_ref_lokasi_child = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        style={'base_template': 'input.html'}
    )

    class Meta:
        model = RefLokasiGD
        fields = '__all__'


class UDRefLokasiGDSerializers(serializers.ModelSerializer):
    queryset = RefLokasiGD.objects.all()

    id_ref_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_lokasi_child = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    class Meta:
        model = RefLokasiGD
        fields = '__all__'
