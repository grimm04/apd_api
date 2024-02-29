from rest_framework import serializers 

from .models import TransTmUidHari   
from apps.master.jaringan.ref_lokasi.models import RefLokasi
from apps.additional.serializers import IDSRef_LokasiSerializer
 

class SubRefParentLokasiSerializer(serializers.ModelSerializer):  
    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi','nama_lokasi']

class TransTmUidHariSerializers(serializers.ModelSerializer):  
     
    id_ref_lokasi_uid = serializers.SlugRelatedField(
        queryset= RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )  
     
    ref_lokasi_uid = IDSRef_LokasiSerializer(read_only=True, source='id_ref_lokasi_uid') 

    class Meta:
        model = TransTmUidHari
        fields = '__all__'
class LaporanBebanUIDHarigHariPDFSerializers(serializers.ModelSerializer):    
    datum  = serializers.DateTimeField(format="%Y-%m-%d %H:%M") 
    ref_lokasi_uid = SubRefParentLokasiSerializer(read_only=True, source='id_ref_lokasi_uid')
    class Meta:
        model = TransTmUidHari
        fields = ['datum','i_avg','i_max','i_max_siang','i_max_malam','p_avg','p_max','p_max_siang','p_max_malam','ref_lokasi_uid','load_faktor']