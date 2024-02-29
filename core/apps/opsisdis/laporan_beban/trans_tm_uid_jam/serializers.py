from rest_framework import serializers 

from .models import TransTmUid  
from apps.additional.serializers import SubRefParentLokasiGISerializer  
from apps.master.jaringan.ref_lokasi.models import RefLokasi

class SubRefParentLokasiSerializer(serializers.ModelSerializer):  
    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi','nama_lokasi']
class LaporanBebanUp3Serializers(serializers.ModelSerializer):   
    lokasi = SubRefParentLokasiGISerializer(read_only=True, source='id_lokasi')
    parent_lokasi = SubRefParentLokasiGISerializer(read_only=True, source='id_parent_lokasi')
    ref_lokasi_uid = SubRefParentLokasiGISerializer(read_only=True, source='id_id_ref_lokasi_uid')
    datum  = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    class Meta:
        model = TransTmUid
        fields = '__all__' 

class LaporanBebanUIDPDFSerializers(serializers.ModelSerializer):    
    datum  = serializers.DateTimeField(format="%Y-%m-%d %H:%M") 
    ref_lokasi_uid = SubRefParentLokasiSerializer(read_only=True, source='id_id_ref_lokasi_uid')  
    class Meta:
        model = TransTmUid
        fields = '__all__' 