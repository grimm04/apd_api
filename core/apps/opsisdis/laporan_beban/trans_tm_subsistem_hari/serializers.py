from rest_framework import serializers 

from .models import TransTmSubsistemHari   
from apps.master.jaringan.ref_lokasi.models import RefLokasi
from apps.additional.serializers import IDSRef_LokasiSerializer

from apps.master.jaringan.ref_lokasi.models import RefLokasi

class SubRefParentLokasiSerializer(serializers.ModelSerializer):  
    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi','nama_lokasi']
 
class TransTmSubsistemHariSerializers(serializers.ModelSerializer):  
     
    id_ref_lokasi_subsistem = serializers.SlugRelatedField(
        queryset= RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )  
     
    ref_lokasi_subsistem = IDSRef_LokasiSerializer(read_only=True, source='id_ref_lokasi_subsistem') 

    class Meta:
        model = TransTmSubsistemHari
        fields = '__all__'

class LaporanBebanSubSistemHarigHariPDFSerializers(serializers.ModelSerializer):    
    datum  = serializers.DateTimeField(format="%Y-%m-%d %H:%M") 
    ref_lokasi_subsistem = SubRefParentLokasiSerializer(read_only=True, source='id_ref_lokasi_subsistem')
    class Meta:
        model = TransTmSubsistemHari
        fields = ['datum','i_avg','i_max','i_max_siang','i_max_malam','p_avg','p_max','p_max_siang','p_max_malam','ref_lokasi_subsistem','load_faktor']