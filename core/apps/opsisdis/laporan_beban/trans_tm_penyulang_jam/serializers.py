from rest_framework import serializers 

from apps.opsisdis.telemetring.penyulang.models import TelemetringPenyulang   
from apps.master.jaringan.ref_lokasi.models import RefLokasi

class SubRefParentLokasiSerializer(serializers.ModelSerializer): 
    nama_parent_lokasi = serializers.CharField(source='nama_lokasi') 
    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi','nama_lokasi', 'nama_parent_lokasi', 'kode_lokasi', 'id_parent_lokasi','no_urut']

class SubRefParentLokasiGISerializer(serializers.ModelSerializer): 
    nama_parent_lokasi = serializers.CharField(source='nama_lokasi')  
    nama_gardu_induk = serializers.SerializerMethodField()  
    class Meta:
        model = RefLokasi 
        fields = ['id_ref_lokasi','nama_lokasi', 'nama_parent_lokasi','kode_lokasi', 'nama_gardu_induk','id_parent_lokasi']

    def get_nama_gardu_induk(self,obj):
        return obj.id_parent_lokasi.nama_lokasi

class LaporanBebanPenyulangSerializers(serializers.ModelSerializer):   
    ref_parent_lokasi = SubRefParentLokasiGISerializer(read_only=True, source='id_parent_lokasi')
    ref_lokasi = SubRefParentLokasiGISerializer(read_only=True, source='id_lokasi')
    datum  = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    date_hari = serializers.DateTimeField(read_only=True, source='datum', format="%Y-%m-%d")
    jam = serializers.DateTimeField(read_only=True, source='datum', format="%H:%M:%S")
    class Meta:
        model = TelemetringPenyulang
        fields = '__all__'
    
class LaporanBebanPenyulangPDFSerializers(serializers.ModelSerializer):    
    datum  = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    ref_parent_lokasi = SubRefParentLokasiGISerializer(read_only=True, source='id_parent_lokasi')
    ref_lokasi = SubRefParentLokasiGISerializer(read_only=True, source='id_lokasi')
    class Meta:
        model = TelemetringPenyulang
        fields = ['datum','i','p','ref_parent_lokasi','ref_lokasi']

class ValidationFilterGISerializer(serializers.Serializer): 
    datum_after  = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    datum_before  = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    jenis_layanan  = serializers.CharField(required=True) 