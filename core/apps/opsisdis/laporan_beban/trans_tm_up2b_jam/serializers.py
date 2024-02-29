from rest_framework import serializers 

from .models import TransTmUp2B  
from apps.additional.serializers import SubRefParentLokasiGISerializer  

from apps.master.jaringan.ref_lokasi.models import RefLokasi
 
class SubRefParentLokasiSerializer(serializers.ModelSerializer):  
    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi','nama_lokasi']
class LaporanBebanUp3Serializers(serializers.ModelSerializer):   
    lokasi = SubRefParentLokasiGISerializer(read_only=True, source='id_lokasi')
    parent_lokasi = SubRefParentLokasiGISerializer(read_only=True, source='id_parent_lokasi')
    id_ref_lokasi_up2b = SubRefParentLokasiGISerializer(read_only=True, source='id_id_ref_lokasi_up2b')
    datum  = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    class Meta:
        model = TransTmUp2B
        fields = '__all__' 

class LaporanBebanUP2BPDFSerializers(serializers.ModelSerializer):    
    datum  = serializers.DateTimeField(format="%Y-%m-%d %H:%M") 
    ref_lokasi_up2b = SubRefParentLokasiSerializer(read_only=True, source='id_id_ref_lokasi_up2b')  
    class Meta:
        model = TransTmUp2B
        fields = '__all__' 