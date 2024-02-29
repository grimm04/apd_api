from rest_framework import serializers

from apps.users.models import Users
from .models import TransJadwalHar
from apps.master.jaringan.ref_lokasi.models import RefLokasi  
from apps.master.opsisdis.ref_jenis_pekerjaan.serializers import RefJenisAliasPekerjaanSerializers 
from apps.additional.serializers import UserDetailSerializerDef
from apps.master.pegawai.perusahaan.serializers import PerusahaanSerializers
from apps.master.pegawai.perusahaan.models import Perusahaan
from apps.opsisdis.jadwal_pemeliharaan.trans_jadwal_har_gardu.models import TransJadwalHarGardu
from apps.additional.serializers import IDSRef_LokasiSerializer 
from apps.master.opsisdis.ref_jenis_pekerjaan.models import RefJenisPekerjaan

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

class TransJadwalHarGarduSerializers(serializers.ModelSerializer):  
    id_gardu = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 
    gardu_induk = ReflokasiGardu(read_only=True, source='id_gardu')   

    class Meta:
        model = TransJadwalHarGardu
        fields = '__all__'

class TransJadwalHarSerializers(serializers.ModelSerializer):  
    id_gardu_induk = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_penyulang = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_gardu = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_up3 = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_jenis_pekerjaan = serializers.SlugRelatedField(
        queryset=RefJenisPekerjaan.objects.all(),
        slug_field='id_ref_jenis_pekerjaan',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    gardu_induk = ReflokasiGI(read_only=True, source='id_gardu_induk') 
    penyulang = ReflokasiPenyulang(read_only=True, source='id_penyulang') 
    gardu = ReflokasiGardu(read_only=True, source='id_gardu') 
    up3 = ReflokasiUp3(read_only=True, source='id_up3') 
    ref_jenis_pekerjaan = RefJenisAliasPekerjaanSerializers(read_only=True, source='id_ref_jenis_pekerjaan') 
    pelaksana = PerusahaanSerializers(read_only=True, source='id_pelaksana') 
    pengawas = UserDetailSerializerDef(read_only=True, source='id_pengawas') 
    user_entri = UserDetailSerializerDef(read_only=True, source='id_user_entri') 
    user_update = UserDetailSerializerDef(read_only=True, source='id_user_update') 
    har_gardu = TransJadwalHarGarduSerializers(many=True,read_only=True)  

    class Meta:
        model = TransJadwalHar
        fields = '__all__'
    
    def get_har_gardu(self, obj):
        return obj.har_gardu.all() 

class CRTransJadwalHarSerializers(serializers.ModelSerializer):  
    id_gardu_induk = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    id_penyulang = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    id_gardu = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    id_up3 = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    id_ref_jenis_pekerjaan = serializers.SlugRelatedField(
        queryset=RefJenisPekerjaan.objects.all(),
        slug_field='id_ref_jenis_pekerjaan',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    ) 
    id_pelaksana = serializers.SlugRelatedField(
        queryset=Perusahaan.objects.all(),
        slug_field='id_perusahaan',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    ) 

    id_pengawas = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        style={'base_template': 'input.html'}
    ) 
    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        style={'base_template': 'input.html'}
    ) 
    
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True, 
        required=False,
        style={'base_template': 'input.html'}
    )  
    tgl_entri = serializers.DateField(format="%Y-%m-%d", read_only=True)
    tgl_update = serializers.DateField(format="%Y-%m-%d", read_only=True)
    
    

    class Meta:
        model = TransJadwalHar
        fields = '__all__'


class UDTransJadwalHarSerializers(serializers.ModelSerializer):
    queryset = TransJadwalHar.objects.all()

    id_gardu_induk = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_penyulang = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_gardu = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_up3 = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_pelaksana = serializers.SlugRelatedField(
        queryset=Perusahaan.objects.all(),
        slug_field='id_perusahaan',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    id_pengawas = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 
    id_ref_jenis_pekerjaan = serializers.SlugRelatedField(
        queryset=RefJenisPekerjaan.objects.all(),
        slug_field='id_ref_jenis_pekerjaan',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False, 
        style={'base_template': 'input.html'}
    ) 
    
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True, 
        required=True,
        style={'base_template': 'input.html'}
    ) 
    
    tgl_entri = serializers.DateField(format="%Y-%m-%d", read_only=True)
    tgl_update = serializers.DateField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = TransJadwalHar
        fields = '__all__'

class UDStatusTransJadwalHarSerializers(serializers.ModelSerializer): 

    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True, 
        required=True,
        style={'base_template': 'input.html'}
    )  
    tgl_update = serializers.DateField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = TransJadwalHar
        fields = ['status_pekerjaan','approval_area1','approval_apd1','id_user_update','keterangan','tgl_update']