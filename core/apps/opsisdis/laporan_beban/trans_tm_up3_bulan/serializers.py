from apps.master.fasop.c_point.serializers import CPoint 
from rest_framework import serializers 

from .models import TransTmUp3Bulan  
from apps.master.jaringan.ref_lokasi.models import RefLokasi
from apps.additional.serializers import IDSRef_LokasiSerializer

class SubRefParentLokasiGISerializer(serializers.ModelSerializer):   
    nama_gardu_induk = serializers.SerializerMethodField()  
    class Meta:
        model = RefLokasi 
        fields = ['id_ref_lokasi','nama_lokasi','kode_lokasi', 'nama_gardu_induk','id_parent_lokasi','id_gardu_induk']

    def get_nama_gardu_induk(self,obj):
        return obj.id_gardu_induk.nama_lokasi

class TransTmUp3BulanSerializers(serializers.ModelSerializer):   
    id_ref_lokasi_up3 = serializers.SlugRelatedField(
        queryset= RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )  
     
    ref_lokasi_up3 = SubRefParentLokasiGISerializer(read_only=True, source='id_ref_lokasi_up3') 

    class Meta:
        model = TransTmUp3Bulan
        fields = '__all__'

class LaporanBebanUp3BulanPDFSerializers(serializers.ModelSerializer):    
    datum  = serializers.DateTimeField(format="%Y-%m-%d %H:%M") 
    ref_lokasi_up3 = SubRefParentLokasiGISerializer(read_only=True, source='id_ref_lokasi_up3')
    class Meta:
        model = TransTmUp3Bulan
        fields = ['datum','i_avg','i_max','i_max_siang','i_max_malam','p_avg','p_max','p_max_siang','p_max_malam','ref_lokasi_gi','ref_lokasi_penyulang','load_faktor']
