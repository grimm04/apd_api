from datetime import datetime
from email.policy import default
from rest_framework import serializers

from .models import WP_ONLINE 
from apps.master.working_permit.wm_bagian.models import WP_BAGIAN 
from apps.working_permit.wp_hirarc.models import WP_HIRARC
from datetime import datetime
from apps.users.models import Users

from apps.additional.serializers import UserDetailSerializerTrans, PerusahaanSerializerTrans,WP_BAGIANSerializer, WP_HIRARCSerializers
from apps.working_permit.wp_master_sop_jsa.models import WP_MASTER_SOP_JSA 
from apps.master.pegawai.perusahaan.models import Perusahaan
from apps.working_permit.wp_sop_perlengkapan.serializers import WPSOPPerlengkapanSerializers
 
 

class WP_MASTERSOPJSASerializer(serializers.ModelSerializer): 

    class Meta:
        model = WP_MASTER_SOP_JSA
        fields = ['id_wp_master_sop_jsa', 'judul_pekerjaan'] 

class WP_ONLINESerializers(serializers.ModelSerializer):  
    nomor_formulir = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    jenis_pekerjaan = serializers.CharField(max_length=50, allow_blank=True, allow_null=True) 
    pekerjaan_dilakukan = serializers.CharField(max_length=200, allow_blank=True, allow_null=True)  
    lokasi_pekerjaan = serializers.CharField(max_length=150, allow_blank=True, allow_null=True) 
    nama_pengawas = serializers.CharField(max_length=150, allow_blank=True, allow_null=True)  
    nama_pengawask3 = serializers.CharField(max_length=150, allow_blank=True, allow_null=True)  
    nama_koordinator_vendor = serializers.CharField(max_length=150, allow_blank=True, allow_null=True) 
    manuver = serializers.BooleanField(default=False)
    grounding = serializers.BooleanField(default=False) 
    petugas_zona1 = serializers.BooleanField(default=False) 
    petugas_zona2 = serializers.BooleanField(default=False) 
    petugas_zona3 = serializers.BooleanField(default=False)  
    klasifikasi1 = serializers.BooleanField(default=False) 
    klasifikasi2 = serializers.BooleanField(default=False) 
    klasifikasi3 = serializers.BooleanField(default=False) 
    klasifikasi4 = serializers.BooleanField(default=False) 
    klasifikasi5 = serializers.BooleanField(default=False) 
    klasifikasi6 = serializers.BooleanField(default=False) 
    klasifikasi7 = serializers.BooleanField(default=False) 
    klasifikasi8 = serializers.BooleanField(default=False) 
    klasifikasi9 = serializers.BooleanField(default=False)  
    klasifikasi10 = serializers.CharField(allow_blank=True, max_length=500)  
    prosedur1 = serializers.BooleanField(default=False) 
    prosedur2 = serializers.BooleanField(default=False) 
    prosedur3 = serializers.BooleanField(default=False) 
    prosedur4 = serializers.BooleanField(default=False) 
    prosedur5 = serializers.BooleanField(default=False) 
    prosedur6 = serializers.BooleanField(default=False) 
    prosedur7 = serializers.BooleanField(default=False) 
    prosedur8 = serializers.BooleanField(default=False) 
    prosedur9 = serializers.BooleanField(default=False)  
    prosedur10 = serializers.CharField(allow_blank=True, max_length=500, required=False) 
    lampiran1 = serializers.BooleanField(default=False) 
    lampiran2 = serializers.BooleanField(default=False) 
    lampiran3 = serializers.BooleanField(default=False) 
    lampiran4 = serializers.BooleanField(default=False) 

    # status_pekerjaan = serializers.CharField(blank=True, max_length=20)  
    status_persetujuan = serializers.IntegerField(required=False, default=None)
    id_wp_on = serializers.CharField(required=False,allow_blank=True, max_length=100) 
    id_bidang = serializers.IntegerField(required=False) 
    qrcode = serializers.CharField(required=False,allow_blank=True, max_length=150) 
    telepon_pengawask3 = serializers.CharField(required=False,allow_blank=True, max_length=20) 
    telepon_pekerja = serializers.CharField(required=False,allow_blank=True, max_length=20) 
    keterangan_reject = serializers.CharField(required=False,allow_blank=True, max_length=1000) 
    jabatan_direksi = serializers.CharField(required=False,allow_blank=True, max_length=150) 
    file_dok = serializers.CharField(required=False,allow_blank=True, max_length=50)  
 
    vendor_pelaksana = serializers.SlugRelatedField( 
        queryset=Perusahaan.objects.all(),
        slug_field='id_perusahaan',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )  

    nomor_sop = serializers.SlugRelatedField( 
        queryset=WP_MASTER_SOP_JSA.objects.all(),
        slug_field='id_wp_master_sop_jsa',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )  

    id_wp_master_bagian = serializers.SlugRelatedField(
        queryset=WP_BAGIAN.objects.all(),
        slug_field='id_wp_master_bagian',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    ) 

    id_user_direksi = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_user_closing = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_wp_hirarc = serializers.SlugRelatedField(
        queryset=WP_HIRARC.objects.all(),
        slug_field='id_wp_hirarc',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    sop_perlengkapan = WPSOPPerlengkapanSerializers(many=True, read_only=True)

    # id_pengawas = serializers.SlugRelatedField(
    #     queryset=Users.objects.all(),
    #     slug_field='id_user',
    #     allow_null=True,
    #     required=False,
    #     style={'base_template': 'input.html'}
    # )
    # id_pengawask3 = serializers.SlugRelatedField(
    #     queryset=Users.objects.all(),
    #     slug_field='id_user',
    #     allow_null=True,
    #     required=False,
    #     style={'base_template': 'input.html'}
    # ) 
    
    id_user_persetujuan = serializers.SlugRelatedField(
       queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )  

    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    tgl_entri = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M:%S" )
    tgl_update = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M:%S" )
    tgl_pekerjaan = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M:%S" ) 
    tgl_pekerjaan_selesai = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M:%S" ) 
    tgl_persetujuan = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M:%S" ) 

    vendor = PerusahaanSerializerTrans(read_only=True, source='vendor_pelaksana') 
    master_sop_jsa = WP_MASTERSOPJSASerializer(read_only=True, source='nomor_sop') 
    bagian = WP_BAGIANSerializer(read_only=True, source='id_wp_master_bagian') 
    user_direksi = UserDetailSerializerTrans(read_only=True, source='id_direksi') 
    user_closing = UserDetailSerializerTrans(read_only=True, source='id_user_closing') 
    wp_hirarc = WP_HIRARCSerializers(read_only=True, source='id_wp_hirarc')  
    user_persetujuan = UserDetailSerializerTrans(read_only=True, source='id_user_persetujuan') 
 
    class Meta:
        model = WP_ONLINE
        fields = '__all__'
        read_only_fields  = ['nomor_formulir']



from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
@extend_schema_serializer(
    exclude_fields=[], # schema ignore these fields
    examples = [
         OpenApiExample(
            'Batch Example',
            summary='Batch Example',
            description='Batch Example',
            value=[
                {
                    "id_wp_online": 0,
                    "nomor_formulir": "string",
                    "jenis_pekerjaan": "string",
                    "pekerjaan_dilakukan": "string",
                    "lokasi_pekerjaan": "string",
                    "nama_pengawas": "string",
                    "nama_pengawask3": "string",
                    "nama_koordinator_vendor": "string",
                    "manuver": False,
                    "grounding": False,
                    "petugas_zona1": False,
                    "petugas_zona2": False,
                    "petugas_zona3": False,
                    "klasifikasi1": False,
                    "klasifikasi2": False,
                    "klasifikasi3": False,
                    "klasifikasi4": False,
                    "klasifikasi5": False,
                    "klasifikasi6": False,
                    "klasifikasi7": False,
                    "klasifikasi8": False,
                    "klasifikasi9": False,
                    "klasifikasi10": "string",
                    "prosedur1": False,
                    "prosedur2": False,
                    "prosedur3": False,
                    "prosedur4": False,
                    "prosedur5": False,
                    "prosedur6": False,
                    "prosedur7": False,
                    "prosedur8": False,
                    "prosedur9": False,
                    "prosedur10": "string",
                    "lampiran1": False,
                    "lampiran2": False,
                    "lampiran3": False,
                    "lampiran4": False,
                    "status_persetujuan": 0,
                    "id_wp_on": "string",
                    "id_bidang": "string",
                    "qrcode": "string",
                    "telepon_pengawask3": "string",
                    "telepon_pekerja": "string",
                    "keterangan_reject": "string",
                    "jabatan_direksi": "string",
                    "file_dok": "string",
                    "vendor_pelaksana": 0,
                    "nomor_sop": 0,
                    "id_wp_master_bagian": 0,
                    "id_user_direksi": 0,
                    "id_user_closing": 0,
                    "id_wp_hirarc": 0,
                    "id_user_persetujuan": 0,
                    "id_user_entri": 0,
                    "id_user_update": 0,
                    "tgl_entri": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_update": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_pekerjaan": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_pekerjaan_selesai": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_persetujuan": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                }, 
                {
                    "id_wp_online": 0,
                    "nomor_formulir": "string",
                    "jenis_pekerjaan": "string",
                    "pekerjaan_dilakukan": "string",
                    "lokasi_pekerjaan": "string",
                    "nama_pengawas": "string",
                    "nama_pengawask3": "string",
                    "nama_koordinator_vendor": "string",
                    "manuver": False,
                    "grounding": False,
                    "petugas_zona1": False,
                    "petugas_zona2": False,
                    "petugas_zona3": False,
                    "klasifikasi1": False,
                    "klasifikasi2": False,
                    "klasifikasi3": False,
                    "klasifikasi4": False,
                    "klasifikasi5": False,
                    "klasifikasi6": False,
                    "klasifikasi7": False,
                    "klasifikasi8": False,
                    "klasifikasi9": False,
                    "klasifikasi10": "string",
                    "prosedur1": False,
                    "prosedur2": False,
                    "prosedur3": False,
                    "prosedur4": False,
                    "prosedur5": False,
                    "prosedur6": False,
                    "prosedur7": False,
                    "prosedur8": False,
                    "prosedur9": False,
                    "prosedur10": "string",
                    "lampiran1": False,
                    "lampiran2": False,
                    "lampiran3": False,
                    "lampiran4": False,
                    "status_persetujuan": 0,
                    "id_wp_on": "string",
                    "id_bidang": "string",
                    "qrcode": "string",
                    "telepon_pengawask3": "string",
                    "telepon_pekerja": "string",
                    "keterangan_reject": "string",
                    "jabatan_direksi": "string",
                    "file_dok": "string",
                    "vendor_pelaksana": 0,
                    "nomor_sop": 0,
                    "id_wp_master_bagian": 0,
                    "id_user_direksi": 0,
                    "id_user_closing": 0,
                    "id_wp_hirarc": 0,
                    "id_user_persetujuan": 0,
                    "id_user_entri": 0,
                    "id_user_update": 0,
                    "tgl_entri": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_update": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_pekerjaan": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_pekerjaan_selesai": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_persetujuan": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                }, 
                 
            ],
            request_only=True, 
            response_only=False,
        ),
         OpenApiExample(
            'Single Example',
            summary='Single Example',
            description='Single Example',
            value=
                {
                    "id_wp_online": 0,
                    "nomor_formulir": "string",
                    "jenis_pekerjaan": "string",
                    "pekerjaan_dilakukan": "string",
                    "lokasi_pekerjaan": "string",
                    "nama_pengawas": "string",
                    "nama_pengawask3": "string",
                    "nama_koordinator_vendor": "string",
                    "manuver": False,
                    "grounding": False,
                    "petugas_zona1": False,
                    "petugas_zona2": False,
                    "petugas_zona3": False,
                    "klasifikasi1": False,
                    "klasifikasi2": False,
                    "klasifikasi3": False,
                    "klasifikasi4": False,
                    "klasifikasi5": False,
                    "klasifikasi6": False,
                    "klasifikasi7": False,
                    "klasifikasi8": False,
                    "klasifikasi9": False,
                    "klasifikasi10": "string",
                    "prosedur1": False,
                    "prosedur2": False,
                    "prosedur3": False,
                    "prosedur4": False,
                    "prosedur5": False,
                    "prosedur6": False,
                    "prosedur7": False,
                    "prosedur8": False,
                    "prosedur9": False,
                    "prosedur10": "string",
                    "lampiran1": False,
                    "lampiran2": False,
                    "lampiran3": False,
                    "lampiran4": False,
                    "status_persetujuan": 0,
                    "id_wp_on": "string",
                    "id_bidang": "string",
                    "qrcode": "string",
                    "telepon_pengawask3": "string",
                    "telepon_pekerja": "string",
                    "keterangan_reject": "string",
                    "jabatan_direksi": "string",
                    "file_dok": "string",
                    "vendor_pelaksana": 0,
                    "nomor_sop": 0,
                    "id_wp_master_bagian": 0,
                    "id_user_direksi": 0,
                    "id_user_closing": 0,
                    "id_wp_hirarc": 0,
                    "id_user_persetujuan": 0,
                    "id_user_entri": 0,
                    "id_user_update": 0,
                    "tgl_entri": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_update": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_pekerjaan": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_pekerjaan_selesai": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_persetujuan": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                },  
            request_only=True, 
            response_only=False,
        ),
    ]
)


class CDWP_ONLINESerializers(serializers.ModelSerializer):

    # nf = serializers.SerializerMethodField(method_name='getItems') 
    nomor_formulir = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    jenis_pekerjaan = serializers.CharField(max_length=50, allow_blank=True, allow_null=True) 
    pekerjaan_dilakukan = serializers.CharField(max_length=200, allow_blank=True, allow_null=True)  
    lokasi_pekerjaan = serializers.CharField(max_length=150, allow_blank=True, allow_null=True) 
    nama_pengawas = serializers.CharField(max_length=150, allow_blank=True, allow_null=True)  
    nama_pengawask3 = serializers.CharField(max_length=150, allow_blank=True, allow_null=True)  
    nama_koordinator_vendor = serializers.CharField(max_length=150, allow_blank=True, allow_null=True) 
    manuver = serializers.BooleanField(default=False)
    grounding = serializers.BooleanField(default=False) 
    petugas_zona1 = serializers.BooleanField(default=False) 
    petugas_zona2 = serializers.BooleanField(default=False) 
    petugas_zona3 = serializers.BooleanField(default=False)  
    klasifikasi1 = serializers.BooleanField(default=False) 
    klasifikasi2 = serializers.BooleanField(default=False) 
    klasifikasi3 = serializers.BooleanField(default=False) 
    klasifikasi4 = serializers.BooleanField(default=False) 
    klasifikasi5 = serializers.BooleanField(default=False) 
    klasifikasi6 = serializers.BooleanField(default=False) 
    klasifikasi7 = serializers.BooleanField(default=False) 
    klasifikasi8 = serializers.BooleanField(default=False) 
    klasifikasi9 = serializers.BooleanField(default=False)  
    klasifikasi10 = serializers.CharField(allow_blank=True, max_length=500)  
    prosedur1 = serializers.BooleanField(default=False) 
    prosedur2 = serializers.BooleanField(default=False) 
    prosedur3 = serializers.BooleanField(default=False) 
    prosedur4 = serializers.BooleanField(default=False) 
    prosedur5 = serializers.BooleanField(default=False) 
    prosedur6 = serializers.BooleanField(default=False) 
    prosedur7 = serializers.BooleanField(default=False) 
    prosedur8 = serializers.BooleanField(default=False) 
    prosedur9 = serializers.BooleanField(default=False)  
    prosedur10 = serializers.CharField(allow_blank=True, max_length=500, required=False) 
    lampiran1 = serializers.BooleanField(default=False) 
    lampiran2 = serializers.BooleanField(default=False) 
    lampiran3 = serializers.BooleanField(default=False) 
    lampiran4 = serializers.BooleanField(default=False) 

    # status_pekerjaan = serializers.CharField(blank=True, max_length=20)  
    status_persetujuan = serializers.IntegerField(required=False, default=0)
    id_wp_on = serializers.CharField(required=False,allow_blank=True, max_length=100) 
    id_bidang = serializers.IntegerField(required=False) 
    qrcode = serializers.CharField(required=False,allow_blank=True, max_length=150) 
    telepon_pengawask3 = serializers.CharField(required=False,allow_blank=True, max_length=20) 
    telepon_pekerja = serializers.CharField(required=False,allow_blank=True, max_length=20) 
    keterangan_reject = serializers.CharField(required=False,allow_blank=True, max_length=1000) 
    jabatan_direksi = serializers.CharField(required=False,allow_blank=True, max_length=150) 
    file_dok = serializers.CharField(required=False,allow_blank=True, max_length=50)  
 
    vendor_pelaksana = serializers.SlugRelatedField( 
        queryset=Perusahaan.objects.all(),
        slug_field='id_perusahaan',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )  

    nomor_sop = serializers.SlugRelatedField( 
        queryset=WP_MASTER_SOP_JSA.objects.all(),
        slug_field='id_wp_master_sop_jsa',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )  

    id_wp_master_bagian = serializers.SlugRelatedField(
        queryset=WP_BAGIAN.objects.all(),
        slug_field='id_wp_master_bagian',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    ) 

    id_user_direksi = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_user_closing = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_wp_hirarc = serializers.SlugRelatedField(
        queryset=WP_HIRARC.objects.all(),
        slug_field='id_wp_hirarc',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    # id_pengawas = serializers.SlugRelatedField(
    #     queryset=Users.objects.all(),
    #     slug_field='id_user',
    #     allow_null=True,
    #     required=False,
    #     style={'base_template': 'input.html'}
    # )
    # id_pengawask3 = serializers.SlugRelatedField(
    #     queryset=Users.objects.all(),
    #     slug_field='id_user',
    #     allow_null=True,
    #     required=False,
    #     style={'base_template': 'input.html'}
    # ) 
    
    id_user_persetujuan = serializers.SlugRelatedField(
       queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )  

    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    tgl_entri = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M:%S" )
    tgl_update = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M:%S" )
    tgl_pekerjaan = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M:%S" ) 
    tgl_pekerjaan_selesai = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M:%S" ) 
    tgl_persetujuan = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M:%S" ) 

    bagian = WP_BAGIANSerializer(read_only=True, source='id_wp_master_bagian') 

    class Meta:
        model = WP_ONLINE
        fields = '__all__' 
        read_only_fields  = ['nomor_formulir'] 


@extend_schema_serializer(
    exclude_fields=[], # schema ignore these fields
    examples = [
         OpenApiExample(
            'Batch Example',
            summary='Batch Example',
            description='Batch Example',
            value=[
                {
                    "id_wp_online": 0,
                    "nomor_formulir": "string",
                    "jenis_pekerjaan": "string",
                    "pekerjaan_dilakukan": "string",
                    "lokasi_pekerjaan": "string",
                    "nama_pengawas": "string",
                    "nama_pengawask3": "string",
                    "nama_koordinator_vendor": "string",
                    "manuver": False,
                    "grounding": False,
                    "petugas_zona1": False,
                    "petugas_zona2": False,
                    "petugas_zona3": False,
                    "klasifikasi1": False,
                    "klasifikasi2": False,
                    "klasifikasi3": False,
                    "klasifikasi4": False,
                    "klasifikasi5": False,
                    "klasifikasi6": False,
                    "klasifikasi7": False,
                    "klasifikasi8": False,
                    "klasifikasi9": False,
                    "klasifikasi10": "string",
                    "prosedur1": False,
                    "prosedur2": False,
                    "prosedur3": False,
                    "prosedur4": False,
                    "prosedur5": False,
                    "prosedur6": False,
                    "prosedur7": False,
                    "prosedur8": False,
                    "prosedur9": False,
                    "prosedur10": "string",
                    "lampiran1": False,
                    "lampiran2": False,
                    "lampiran3": False,
                    "lampiran4": False,
                    "status_persetujuan": 0,
                    "id_wp_on": "string",
                    "id_bidang": "string",
                    "qrcode": "string",
                    "telepon_pengawask3": "string",
                    "telepon_pekerja": "string",
                    "keterangan_reject": "string",
                    "jabatan_direksi": "string",
                    "file_dok": "string",
                    "vendor_pelaksana": 0,
                    "nomor_sop": 0,
                    "id_wp_master_bagian": 0,
                    "id_user_direksi": 0,
                    "id_user_closing": 0,
                    "id_wp_hirarc": 0,
                    "id_user_persetujuan": 0,
                    "id_user_entri": 0,
                    "id_user_update": 0,
                    "tgl_entri": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_update": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_pekerjaan": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_pekerjaan_selesai": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_persetujuan": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                }, 
                {
                    "id_wp_online": 0,
                    "nomor_formulir": "string",
                    "jenis_pekerjaan": "string",
                    "pekerjaan_dilakukan": "string",
                    "lokasi_pekerjaan": "string",
                    "nama_pengawas": "string",
                    "nama_pengawask3": "string",
                    "nama_koordinator_vendor": "string",
                    "manuver": False,
                    "grounding": False,
                    "petugas_zona1": False,
                    "petugas_zona2": False,
                    "petugas_zona3": False,
                    "klasifikasi1": False,
                    "klasifikasi2": False,
                    "klasifikasi3": False,
                    "klasifikasi4": False,
                    "klasifikasi5": False,
                    "klasifikasi6": False,
                    "klasifikasi7": False,
                    "klasifikasi8": False,
                    "klasifikasi9": False,
                    "klasifikasi10": "string",
                    "prosedur1": False,
                    "prosedur2": False,
                    "prosedur3": False,
                    "prosedur4": False,
                    "prosedur5": False,
                    "prosedur6": False,
                    "prosedur7": False,
                    "prosedur8": False,
                    "prosedur9": False,
                    "prosedur10": "string",
                    "lampiran1": False,
                    "lampiran2": False,
                    "lampiran3": False,
                    "lampiran4": False,
                    "status_persetujuan": 0,
                    "id_wp_on": "string",
                    "id_bidang": "string",
                    "qrcode": "string",
                    "telepon_pengawask3": "string",
                    "telepon_pekerja": "string",
                    "keterangan_reject": "string",
                    "jabatan_direksi": "string",
                    "file_dok": "string",
                    "vendor_pelaksana": 0,
                    "nomor_sop": 0,
                    "id_wp_master_bagian": 0,
                    "id_user_direksi": 0,
                    "id_user_closing": 0,
                    "id_wp_hirarc": 0,
                    "id_user_persetujuan": 0,
                    "id_user_entri": 0,
                    "id_user_update": 0,
                    "tgl_entri": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_update": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_pekerjaan": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_pekerjaan_selesai": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_persetujuan": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                }, 
            ],
            request_only=True, 
            response_only=False,
        ),
         OpenApiExample(
            'Single Example',
            summary='Single Example',
            description='Single Example',
            value=
                {
                    "id_wp_online": 0,
                    "nomor_formulir": "string",
                    "jenis_pekerjaan": "string",
                    "pekerjaan_dilakukan": "string",
                    "lokasi_pekerjaan": "string",
                    "nama_pengawas": "string",
                    "nama_pengawask3": "string",
                    "nama_koordinator_vendor": "string",
                    "manuver": False,
                    "grounding": False,
                    "petugas_zona1": False,
                    "petugas_zona2": False,
                    "petugas_zona3": False,
                    "klasifikasi1": False,
                    "klasifikasi2": False,
                    "klasifikasi3": False,
                    "klasifikasi4": False,
                    "klasifikasi5": False,
                    "klasifikasi6": False,
                    "klasifikasi7": False,
                    "klasifikasi8": False,
                    "klasifikasi9": False,
                    "klasifikasi10": "string",
                    "prosedur1": False,
                    "prosedur2": False,
                    "prosedur3": False,
                    "prosedur4": False,
                    "prosedur5": False,
                    "prosedur6": False,
                    "prosedur7": False,
                    "prosedur8": False,
                    "prosedur9": False,
                    "prosedur10": "string",
                    "lampiran1": False,
                    "lampiran2": False,
                    "lampiran3": False,
                    "lampiran4": False,
                    "status_persetujuan": 0,
                    "id_wp_on": "string",
                    "id_bidang": "string",
                    "qrcode": "string",
                    "telepon_pengawask3": "string",
                    "telepon_pekerja": "string",
                    "keterangan_reject": "string",
                    "jabatan_direksi": "string",
                    "file_dok": "string",
                    "vendor_pelaksana": 0,
                    "nomor_sop": 0,
                    "id_wp_master_bagian": 0,
                    "id_user_direksi": 0,
                    "id_user_closing": 0,
                    "id_wp_hirarc": 0,
                    "id_user_persetujuan": 0,
                    "id_user_entri": 0,
                    "id_user_update": 0,
                    "tgl_entri": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_update": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_pekerjaan": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_pekerjaan_selesai": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                    "tgl_persetujuan": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                },  
            request_only=True, 
            response_only=False,
        ),
    ]
)
class UDWP_ONLINESerializers(serializers.ModelSerializer):
    nomor_formulir = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    jenis_pekerjaan = serializers.CharField(max_length=50, allow_blank=True, allow_null=True) 
    pekerjaan_dilakukan = serializers.CharField(max_length=200, allow_blank=True, allow_null=True)  
    lokasi_pekerjaan = serializers.CharField(max_length=150, allow_blank=True, allow_null=True) 
    nama_pengawas = serializers.CharField(max_length=150, allow_blank=True, allow_null=True)  
    nama_pengawask3 = serializers.CharField(max_length=150, allow_blank=True, allow_null=True)  
    nama_koordinator_vendor = serializers.CharField(max_length=150, allow_blank=True, allow_null=True) 
    manuver = serializers.BooleanField(default=False)
    grounding = serializers.BooleanField(default=False) 
    petugas_zona1 = serializers.BooleanField(default=False) 
    petugas_zona2 = serializers.BooleanField(default=False) 
    petugas_zona3 = serializers.BooleanField(default=False)  
    klasifikasi1 = serializers.BooleanField(default=False) 
    klasifikasi2 = serializers.BooleanField(default=False) 
    klasifikasi3 = serializers.BooleanField(default=False) 
    klasifikasi4 = serializers.BooleanField(default=False) 
    klasifikasi5 = serializers.BooleanField(default=False) 
    klasifikasi6 = serializers.BooleanField(default=False) 
    klasifikasi7 = serializers.BooleanField(default=False) 
    klasifikasi8 = serializers.BooleanField(default=False) 
    klasifikasi9 = serializers.BooleanField(default=False)  
    klasifikasi10 = serializers.CharField(allow_blank=True, max_length=500)  
    prosedur1 = serializers.BooleanField(default=False) 
    prosedur2 = serializers.BooleanField(default=False) 
    prosedur3 = serializers.BooleanField(default=False) 
    prosedur4 = serializers.BooleanField(default=False) 
    prosedur5 = serializers.BooleanField(default=False) 
    prosedur6 = serializers.BooleanField(default=False) 
    prosedur7 = serializers.BooleanField(default=False) 
    prosedur8 = serializers.BooleanField(default=False) 
    prosedur9 = serializers.BooleanField(default=False)  
    prosedur10 = serializers.CharField(allow_blank=True, max_length=500, required=False) 
    lampiran1 = serializers.BooleanField(default=False) 
    lampiran2 = serializers.BooleanField(default=False) 
    lampiran3 = serializers.BooleanField(default=False) 
    lampiran4 = serializers.BooleanField(default=False) 

    # status_pekerjaan = serializers.CharField(blank=True, max_length=20)  
    status_persetujuan = serializers.IntegerField(required=False, default=None)
    id_wp_on = serializers.CharField(required=False,allow_blank=True, max_length=100) 
    id_bidang = serializers.IntegerField(required=False) 
    qrcode = serializers.CharField(required=False,allow_blank=True, max_length=150) 
    telepon_pengawask3 = serializers.CharField(required=False,allow_blank=True, max_length=20) 
    telepon_pekerja = serializers.CharField(required=False,allow_blank=True, max_length=20) 
    keterangan_reject = serializers.CharField(required=False,allow_blank=True, max_length=1000) 
    jabatan_direksi = serializers.CharField(required=False,allow_blank=True, max_length=150) 
    file_dok = serializers.CharField(required=False,allow_blank=True, max_length=50)  
 
    vendor_pelaksana = serializers.SlugRelatedField( 
        queryset=Perusahaan.objects.all(),
        slug_field='id_perusahaan',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )  

    nomor_sop = serializers.SlugRelatedField( 
        queryset=WP_MASTER_SOP_JSA.objects.all(),
        slug_field='id_wp_master_sop_jsa',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )  

    id_wp_master_bagian = serializers.SlugRelatedField(
        queryset=WP_BAGIAN.objects.all(),
        slug_field='id_wp_master_bagian',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    ) 

    id_user_direksi = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_user_closing = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_wp_hirarc = serializers.SlugRelatedField(
        queryset=WP_HIRARC.objects.all(),
        slug_field='id_wp_hirarc',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    # id_pengawas = serializers.SlugRelatedField(
    #     queryset=Users.objects.all(),
    #     slug_field='id_user',
    #     allow_null=True,
    #     required=False,
    #     style={'base_template': 'input.html'}
    # )
    # id_pengawask3 = serializers.SlugRelatedField(
    #     queryset=Users.objects.all(),
    #     slug_field='id_user',
    #     allow_null=True,
    #     required=False,
    #     style={'base_template': 'input.html'}
    # ) 
    
    id_user_persetujuan = serializers.SlugRelatedField(
       queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )  

    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    tgl_entri = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M:%S" )
    tgl_update = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M:%S" )
    tgl_pekerjaan = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M:%S" ) 
    tgl_pekerjaan_selesai = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M:%S" ) 
    tgl_persetujuan = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M:%S" ) 

    class Meta:
        model = WP_ONLINE
        fields = '__all__'
        read_only_fields  = ['nomor_formulir']

@extend_schema_serializer(
    exclude_fields=[], # schema ignore these fields
    examples = [ 
         OpenApiExample(
            'Example',
            summary='Example',
            description='Example',
            value=
                { 
                    "status_persetujuan": 0, 
                    "id_user_update": 0,   
                },  
            request_only=True, 
            response_only=False,
        ),
    ]
)
class UDAPROVALWP_ONLINESerializers(serializers.ModelSerializer): 
    status_persetujuan = serializers.IntegerField(required=True)  
    # status_pekerjaan = serializers.IntegerField(required=True)  
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    ) 
    tgl_update = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M:%S" , read_only=True) 
    tgl_persetujuan = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=None) 

    class Meta:
        model = WP_ONLINE
        fields = ['id_wp_online','status_persetujuan','id_user_update','tgl_update','tgl_persetujuan'] 
        read_only_fields  = ['tgl_update']



class UDREJECTWP_ONLINESerializers(serializers.ModelSerializer): 
    keterangan_reject = serializers.CharField(required=False,allow_blank=True, max_length=1000)  
    status_persetujuan = serializers.IntegerField(required=True)  
    # status_pekerjaan = serializers.IntegerField(required=True)  
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    ) 
    # tgl_update = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M:%S" ) 
    # tgl_persetujuan = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=True, allow_null=True) 

    class Meta:
        model = WP_ONLINE
        fields = ['id_wp_online','status_persetujuan','id_user_update','keterangan_reject'] 
        # read_only_fields  = ['tgl_update']





