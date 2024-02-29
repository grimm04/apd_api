from rest_framework import serializers 

from .models import TransTmUp3Jam  
from apps.additional.serializers import SubRefParentLokasiGISerializer  
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
        fields = ['id_ref_lokasi','nama_lokasi', 'nama_parent_lokasi','kode_lokasi', 'nama_gardu_induk','id_parent_lokasi','id_gardu_induk']

    def get_nama_gardu_induk(self,obj):
        return obj.id_gardu_induk.nama_lokasi

class LaporanBebanUp3Serializers(serializers.ModelSerializer):   
    lokasi = SubRefParentLokasiSerializer(read_only=True, source='id_lokasi')
    parent_lokasi = SubRefParentLokasiGISerializer(read_only=True, source='id_parent_lokasi')
    ref_lokasi_up3 = SubRefParentLokasiGISerializer(read_only=True, source='id_ref_lokasi_up3')
    datum  = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    class Meta:
        model = TransTmUp3Jam
        fields = '__all__' 

class LaporanBebanUp3PDFSerializers(serializers.ModelSerializer):    
    datum  = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    ref_parent_lokasi = SubRefParentLokasiGISerializer(read_only=True, source='id_parent_lokasi')
    ref_lokasi_up3 = SubRefParentLokasiGISerializer(read_only=True, source='id_ref_lokasi_up3') 
    datum  = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    class Meta:
        model = TransTmUp3Jam
        fields = '__all__' 