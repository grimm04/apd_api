from pyexpat import model
from rest_framework import serializers

from apps.users.models import Users 

from apps.master.fasop.c_point.models import CPoint 
from apps.master.fasop.point_type.models import PointType
from apps.master.fasop.master.models import FASOPMASTER 
from apps.master.fasop.rtu.models import RTU 
from apps.master.jaringan.ref_lokasi.models import RefLokasi
from apps.master.pegawai.perusahaan.models import Perusahaan
from apps.master.working_permit.wm_bagian.models import WP_BAGIAN
from apps.master.jaringan.ref_jenis_lokasi.models import RefJenisLokasi
from apps.master.aset.ref_aset_jenis.models import RefAsetJenis
from apps.master.opsisdis.pm.ref_pm.models import RefPM
from apps.master.opsisdis.pm.ref_pm_detail.models import RefPMDetail

from apps.working_permit.wp_hirarc.models import WP_HIRARC 
from apps.master.working_permit.wm_bagian.models import WP_BAGIAN 
 
from apps.master.fasop.telegram_group.models import TelegramGroup
from django_filters import rest_framework

class CharInFilter(rest_framework.BaseInFilter, rest_framework.CharFilter):
    pass

class NumberInFilter(rest_framework.BaseInFilter, rest_framework.NumberFilter):
    pass

class ReflokasiGI(serializers.ModelSerializer): 
    nama_gardu_induk = serializers.CharField(source='nama_lokasi')   
    class Meta:
        model = RefLokasi 
        fields = ['id_ref_lokasi','nama_lokasi', 'nama_gardu_induk']
class ReflokasiPenyulang(serializers.ModelSerializer): 
    nama_penyulang = serializers.CharField(source='nama_lokasi')   
    class Meta:
        model = RefLokasi 
        fields = ['id_ref_lokasi','nama_lokasi', 'nama_penyulang']
class ReflokasiSection(serializers.ModelSerializer): 
    nama_section = serializers.CharField(source='nama_lokasi')   
    class Meta:
        model = RefLokasi 
        fields = ['id_ref_lokasi','nama_lokasi', 'nama_section']

class ReflokasiZone(serializers.ModelSerializer): 
    nama_zone = serializers.CharField(source='nama_lokasi')   
    class Meta:
        model = RefLokasi 
        fields = ['id_ref_lokasi','nama_lokasi', 'nama_zone']
class ReflokasiGardu(serializers.ModelSerializer): 
    nama_gardu = serializers.CharField(source='nama_lokasi')   
    class Meta:
        model = RefLokasi 
        fields = ['id_ref_lokasi','nama_lokasi', 'nama_gardu']
class ReflokasiUp3(serializers.ModelSerializer): 
    nama_up3 = serializers.CharField(source='nama_lokasi')   
    class Meta:
        model = RefLokasi 
        fields = ['id_ref_lokasi','nama_lokasi', 'nama_up3']
class ReflokasiZone(serializers.ModelSerializer): 
    nama_zone = serializers.CharField(source='nama_lokasi')   
    class Meta:
        model = RefLokasi 
        fields = ['id_ref_lokasi','nama_lokasi', 'nama_zone'] 
class ReflokasiUlp(serializers.ModelSerializer): 
    nama_ulp = serializers.CharField(source='nama_lokasi')   
    class Meta:
        model = RefLokasi 
        fields = ['id_ref_lokasi','nama_lokasi', 'nama_ulp']

class SubTelegramGroupSerializer(serializers.ModelSerializer):
    nama_group = serializers.CharField(source='nama')
    class Meta:
        model = TelegramGroup
        fields = ['nama', 'id_chat','nama_group']


class GetParentRef_lokasi(serializers.ModelSerializer):
    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi','nama_lokasi'] 
class RefJenisLokasierializer(serializers.ModelSerializer):
    class Meta:
        model = RefJenisLokasi
        fields = ['id_ref_jenis_lokasi', 'nama_jenis_lokasi']

class IDSRef_LokasiSerializer(serializers.ModelSerializer):
    ref_jenis_lokasi = RefJenisLokasierializer(read_only=True, source='id_ref_jenis_lokasi')
    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi', 'nama_lokasi', 'kode_lokasi','ref_jenis_lokasi','no_urut','jenis_layanan','pemilik']  


class RefLokasiWParentSerializer(serializers.ModelSerializer): 
    parent_lokasi = GetParentRef_lokasi(read_only=True, source='id_parent_lokasi')  
    nama_gardu_induk = serializers.SerializerMethodField() 
    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi', 'id_parent_lokasi','nama_lokasi','parent_lokasi','nama_gardu_induk']  

    def get_nama_gardu_induk(self,obj):
        return obj.id_parent_lokasi.nama_lokasi
    


class SubRefParentLokasiSerializer(serializers.ModelSerializer):

    nama_parent_lokasi = serializers.CharField(source='nama_lokasi')
    
    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi','nama_lokasi', 'nama_parent_lokasi', 'kode_lokasi', 'id_parent_lokasi','no_urut']

class SubRefParentLokasiGISerializer(serializers.ModelSerializer):
    parent_lokasi = SubRefParentLokasiSerializer(read_only=True, source='id_parent_lokasi') 
    nama_parent_lokasi = serializers.CharField(source='nama_lokasi')  
    class Meta:
        model = RefLokasi 
        fields = ['id_ref_lokasi','nama_lokasi', 'nama_parent_lokasi','kode_lokasi', 'id_parent_lokasi','no_urut','parent_lokasi','jenis_layanan','sinkron_data','def_pengukuran_teg_primer','def_pengukuran_teg_sekunder','def_nilai_cosq']
class IDSRef_LokasiADDSerializer(serializers.ModelSerializer):
    ref_jenis_lokasi = RefJenisLokasierializer(read_only=True, source='id_ref_jenis_lokasi')
    up3_1 = SubRefParentLokasiSerializer(read_only=True, source='id_up3_1')   
    nama_parent_lokasi = serializers.CharField(source='nama_lokasi')  
    nama_area = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi', 'nama_lokasi', 'kode_lokasi','ref_jenis_lokasi','no_urut','up3_1','nama_parent_lokasi','nama_area'] 
    
    def get_nama_area(self, obj):
        return obj.id_up3_1.nama_lokasi

class SubPointTypeSerializer(serializers.ModelSerializer): 
    class Meta:
        model = PointType
        fields = ['id_pointtype', 'name', 'jenispoint', 'warna']

class CPointTypeSerializer(serializers.ModelSerializer): 
    pointtype = SubPointTypeSerializer(read_only=True, source='id_pointtype') 
    class Meta:
        model = CPoint
        fields = ['id_pointtype','point_number', 'point_name', 'point_type','path1','path2','path3','path4','path5','path1text','path2text','path3text','path4text','path5text','pointtype','pointtype_name'] 

class UserDetailSerializerDef(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id_user', 'nip', 'fullname'] 

class UserDetailSerializerTrans(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id_user', 'fullname'] 

class PerusahaanSerializerTrans(serializers.ModelSerializer):
    class Meta:
        model = Perusahaan
        fields = ['id_perusahaan', 'nama','nama_direktur'] 
 
class FASOPMASTERTypeSerializer(serializers.ModelSerializer): 
    pointtype = SubPointTypeSerializer(read_only=True, source='id_pointtype')
    ref_lokasi = IDSRef_LokasiSerializer(read_only=True, source='id_ref_lokasi')
    class Meta:
        model = FASOPMASTER
        fields = ['point_number', 'path3text', 'id_ref_lokasi','path3','pointtype','ref_lokasi'] 


class RTUTypeSerializer(serializers.ModelSerializer): 
    pointtype = SubPointTypeSerializer(read_only=True, source='id_pointtype')
    ref_lokasi = IDSRef_LokasiSerializer(read_only=True, source='id_ref_lokasi')
    class Meta:
        model = RTU
        fields = ['point_number', 'path3text', 'id_ref_lokasi','path3','pointtype','ref_lokasi','pointtype_name'] 


#WP

class WP_BAGIANSerializer(serializers.ModelSerializer):

    class Meta:
        model = WP_BAGIAN
        fields = ['id_wp_master_bagian', 'name','ept']

class WP_HIRARCSerializers(serializers.ModelSerializer):
    pekerjaan = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
    lokasi_pekerjaan = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    tanggal = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None) 
    
    id_wp_master_bagian = serializers.SlugRelatedField(
        queryset=WP_BAGIAN.objects.all(),
        slug_field='id_wp_master_bagian',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    bagian = WP_BAGIANSerializer(read_only=True, source='id_wp_master_bagian') 

    class Meta:
        model = WP_HIRARC
        fields = '__all__'
        

class RefAsetJenisSerializers(serializers.ModelSerializer):
    class Meta:
        model = RefAsetJenis
        fields = ['id_ref_aset_jenis', 'nama_aset_jenis', 'status']

class RefPMSerializers(serializers.ModelSerializer):
    class Meta:
        model = RefPM
        fields = ['id_ref_pm', 'nama', 'level_pm','status']

class RefPMDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = RefPMDetail
        fields = ['id_ref_pm_detail', 'nama', 'satuan', 'id_induk_ref_pm_detail', 'induk', 'nilai_acuan', 'no_urut', 'tipe_data','nilai_pemeriksaan']