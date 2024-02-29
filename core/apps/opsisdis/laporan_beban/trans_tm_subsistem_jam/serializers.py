from rest_framework import serializers 

from .models import TransTmSubsistem  
from apps.additional.serializers import SubRefParentLokasiGISerializer  
from apps.master.jaringan.ref_lokasi.models import RefLokasi
 
class SubRefParentLokasiSerializer(serializers.ModelSerializer):  
    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi','nama_lokasi']
 
class LaporanBebanUp3Serializers(serializers.ModelSerializer):   
    lokasi = SubRefParentLokasiGISerializer(read_only=True, source='id_lokasi')
    parent_lokasi = SubRefParentLokasiGISerializer(read_only=True, source='id_parent_lokasi')
    ref_lokasi_subsistem = SubRefParentLokasiGISerializer(read_only=True, source='id_ref_lokasi_subsistem')
    datum  = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    class Meta:
        model = TransTmSubsistem
        fields = '__all__' 

class LaporanBebanUp3PDFSerializers(serializers.ModelSerializer):    
    datum  = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    ref_parent_lokasi = SubRefParentLokasiGISerializer(read_only=True, source='id_parent_lokasi')
    ref_lokasi_subsistem = SubRefParentLokasiSerializer(read_only=True, source='id_ref_lokasi_subsistem')  
    class Meta:
        model = TransTmSubsistem
        fields = '__all__' 