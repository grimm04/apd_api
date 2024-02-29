from rest_framework import serializers 

from apps.opsisdis.telemetring.trafo_gi_non_ktt.models import TelemetringTrafoGI  
# from apps.additional.serializers import SubRefParentLokasiGISerializer  
from apps.master.jaringan.ref_lokasi.models import RefLokasi

class SubRefParentLokasiSerializer(serializers.ModelSerializer): 
    nama_parent_lokasi = serializers.CharField(source='nama_lokasi') 
    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi','nama_lokasi', 'nama_parent_lokasi', 'kode_lokasi', 'id_parent_lokasi','no_urut']

class SubRefParentLokasiGISerializer(serializers.ModelSerializer): 
    nama_gardu_induk = serializers.CharField(source='nama_lokasi')    
    class Meta:
        model = RefLokasi 
        fields = ['id_ref_lokasi','nama_lokasi','kode_lokasi', 'nama_gardu_induk','id_parent_lokasi','no_urut']
 
 
class LaporanBebanTrafoGISerializers(serializers.ModelSerializer):  
    ref_lokasi = SubRefParentLokasiSerializer(read_only=True, source='id_lokasi')
    ref_parent_lokasi = SubRefParentLokasiGISerializer(read_only=True, source='id_parent_lokasi') 
    datum  = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    date_hari = serializers.DateTimeField(read_only=True, source='datum', format="%Y-%m-%d")
    jam = serializers.DateTimeField(read_only=True, source='datum', format="%H:%M:%S")
    class Meta:
        model = TelemetringTrafoGI
        fields = '__all__'
class ValidationFilterGISerializer(serializers.Serializer): 
    datum_after  = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    datum_before  = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    jenis_layanan  = serializers.CharField(required=True) 

class LaporanBebanTrafoGIPDFSerializers(serializers.ModelSerializer):    
    datum  = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    ref_lokasi = SubRefParentLokasiGISerializer(read_only=True, source='id_lokasi')
    ref_parent_lokasi = SubRefParentLokasiGISerializer(read_only=True, source='id_parent_lokasi') 
    class Meta:
        model = TelemetringTrafoGI
        fields = ['datum','i','p','ref_lokasi','ref_parent_lokasi']