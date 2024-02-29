from numpy import source
from rest_framework import serializers

from apps.users.models import Users
from apps.master.jaringan.ref_jenis_lokasi.models import RefJenisLokasi

from .models import RefLokasi, RefLokasiTemp
from apps.master.jaringan.ref_jenis_pembangkit.models import RefJenisPembangkit 
from apps.master.wilayah.ref_province.models import RefProvince
from apps.master.wilayah.ref_regency.models import RefRegency 
from apps.master.wilayah.ref_district.models import RefDistrict
from apps.master.jaringan.ref_jenis_lokasi.serializers import RefJenisLokasierializer
from apps.master.wilayah.ref_province.serializers import RefProvincSerializers
from apps.master.wilayah.ref_regency.serializers import RefRegencyerializer
from apps.master.wilayah.ref_district.serializers import RefDistricterializer 
from apps.master.jaringan.ref_jenis_pembangkit.serializers import RefJenisPembangkiterializer

class IDParentGetIDSerializer(serializers.ModelSerializer): 
    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi','id_parent_lokasi', 'nama_lokasi'] 



class IDSRef_LokasiSerializer(serializers.ModelSerializer):
    parent_lokasi = IDParentGetIDSerializer(read_only=True, source='id_parent_lokasi') 
    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi','id_parent_lokasi', 'nama_lokasi', 'kode_lokasi','no_urut','jenis_layanan','sinkron_data','def_pengukuran_teg_primer','def_pengukuran_teg_sekunder','def_nilai_cosq','parent_lokasi'] 


class RefLokasiSerializerGeneratePengukuran(serializers.ModelSerializer): 
    parent_lokasi = IDSRef_LokasiSerializer(read_only=True, source='id_parent_lokasi') 
    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi','id_parent_lokasi', 'nama_lokasi', 'kode_lokasi','no_urut','jenis_layanan','sinkron_data','def_pengukuran_teg_primer','def_pengukuran_teg_sekunder','def_nilai_cosq','parent_lokasi'] 



class RefLokasiSerializer(serializers.ModelSerializer):  
    ref_jenis_lokasi = RefJenisLokasierializer(read_only=True, source='id_ref_jenis_lokasi')
    parent_lokasi = IDSRef_LokasiSerializer(read_only=True, source='id_parent_lokasi')
    uid = IDSRef_LokasiSerializer(read_only=True, source='id_uid')
    up3_1 = IDSRef_LokasiSerializer(read_only=True,  source='id_up3_1')
    up3_2 = IDSRef_LokasiSerializer(read_only=True,  source='id_up3_2')
    ulp_1 = IDSRef_LokasiSerializer(read_only=True,  source='id_ulp_1')
    ulp_2 = IDSRef_LokasiSerializer(read_only=True,  source='id_ulp_2')
    up2b = IDSRef_LokasiSerializer(read_only=True,  source='id_up2b')
    penyulang = IDSRef_LokasiSerializer(read_only=True,  source='id_penyulang')
    section = IDSRef_LokasiSerializer(read_only=True,  source='id_section')
    segment = IDSRef_LokasiSerializer(read_only=True,  source='id_segment')
    zone = IDSRef_LokasiSerializer(read_only=True,  source='id_zone')
    unit_pembangkit = IDSRef_LokasiSerializer(read_only=True,  source='id_unit_pembangkit')
    pembangkit = IDSRef_LokasiSerializer(read_only=True,  source='id_pembangkit')
    gardu_induk = IDSRef_LokasiSerializer(read_only=True,  source='id_gardu_induk')
    trafo_gi = IDSRef_LokasiSerializer(read_only=True,  source='id_trafo_gi')
    gardu_distribusi = IDSRef_LokasiSerializer(read_only=True,  source='id_gardu_distribusi')
    trafo_gd = IDSRef_LokasiSerializer(read_only=True,  source='id_trafo_gd')
    gardu_hubung = IDSRef_LokasiSerializer(read_only=True, source='id_gardu_hubung')
    ref_province = RefProvincSerializers(read_only=True, source='id_ref_province')
    ref_regency = RefRegencyerializer(read_only=True, source='id_ref_regency')
    ref_district = RefDistricterializer(read_only=True, source='id_ref_district')
    ref_jenis_pembangkit = RefJenisPembangkiterializer(read_only=True, source='id_ref_jenis_pembangkit')
    count_gardu = serializers.SerializerMethodField(read_only=True, source='children')

    # children  = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = RefLokasi
        # fields = ( 
        #    'id_parent_lokasi', 'id_ref_jenis_lokasi', 'id_user_entri','id_user_update',
        #           'tree_jaringan', 'coverage', 'kva', 'phase', 'status_listrik', 'no_tiang','status_listrik',
        #           'jenis_jaringan', 'status_penyulang', 'count_gardu','id_uid','id_up3','id_ulp', 'id_penyulang','id_zone','id_section','id_segment',
        #     'ref_lokasi_child')
        fields = '__all__'

    def get_children(self):
        return RefLokasi.objects.get(tree_jaringan=1)

    def get_count_gardu(self, obj):
        return obj.children.count()


class CRRefLokasiSerializers(serializers.ModelSerializer):
    nama_lokasi = serializers.CharField(max_length=100)
    kode_lokasi = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    jumlah_pelanggan = serializers.IntegerField(default=None, allow_null=True)
    jumlah_jurusan = serializers.IntegerField(default=None, allow_null=True)
    jenis_trafo = serializers.CharField(max_length=20, default=None, allow_blank=True, allow_null=True)
    fungsi_scada = serializers.CharField(max_length=20, allow_blank=True, allow_null=True, required=False)
    kapasitas = serializers.IntegerField(required=False,default=None, allow_null=True)
    sub_sistem = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, required=False)
    pemilik = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, required=False)
    status_trafo = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, required=False)
    i_max = serializers.IntegerField(required=False,default=None, allow_null=True)
    ratio_ct = serializers.IntegerField(required=False,default=None, allow_null=True)
    ratio_vt = serializers.IntegerField(required=False,default=None, allow_null=True)
    fk_meter_pembanding = serializers.IntegerField(required=False,default=None, allow_null=True)
    primer_tegangan_max = serializers.IntegerField(required=False,default=None, allow_null=True)
    primer_tegangan_min = serializers.IntegerField(required=False,default=None, allow_null=True)
    sekunder_tegangan_min = serializers.IntegerField(required=False,default=None, allow_null=True)
    sekunder_tegangan_max = serializers.IntegerField(required=False,default=None, allow_null=True)
    sinkron_data = serializers.CharField(max_length=50, allow_blank=True, allow_null=True, required=False)
    jenis_layanan = serializers.CharField(max_length=50, allow_blank=True, allow_null=True, required=False)
    id_i = serializers.IntegerField(required=False,default=None, allow_null=True)
    id_v = serializers.IntegerField(required=False,default=None, allow_null=True)
    id_p = serializers.IntegerField(required=False,default=None, allow_null=True)
    id_amr = serializers.IntegerField(required=False,default=None, allow_null=True)
    id_portal_ext = serializers.IntegerField(required=False,default=None, allow_null=True)
    url_webservice = serializers.CharField(max_length=255, allow_blank=True, allow_null=True, required=False)
    jenis_gi = serializers.CharField(max_length=50, allow_blank=True, allow_null=True, required=False)
    faktor_meter = serializers.IntegerField(required=False,default=None, allow_null=True)
    faktor_kali = serializers.IntegerField(required=False,default=None, allow_null=True)
    dcc = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, required=False) 
    def_pengukuran_teg_primer = serializers.DecimalField(default=150,max_digits=5, decimal_places=2,required=False) 
    def_pengukuran_teg_sekunder = serializers.DecimalField(default=20.5,max_digits=5, decimal_places=2,required=False) 
    def_nilai_cosq = serializers.DecimalField(default=0.95,max_digits=5, decimal_places=2,required=False)  
    

    id_penyulang = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_zone = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_section = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_segment = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    id_parent_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_jenis_lokasi = serializers.SlugRelatedField(
        queryset=RefJenisLokasi.objects.all(),
        slug_field='id_ref_jenis_lokasi',
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
    id_uid = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_up3_1 = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_up3_2 = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ulp_1 = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ulp_2 = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_up2b = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    id_unit_pembangkit = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    id_pembangkit = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    id_gardu_induk = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    id_trafo_gi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    id_gardu_distribusi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    id_trafo_gd = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_gardu_hubung = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_province = serializers.SlugRelatedField(
        queryset=RefProvince.objects.all(),
        slug_field='id_ref_province',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_regency = serializers.SlugRelatedField(
        queryset=RefRegency.objects.all(),
        slug_field='id_ref_regency',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_district = serializers.SlugRelatedField(
        queryset=RefDistrict.objects.all(),
        slug_field='id_ref_district',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_jenis_pembangkit = serializers.SlugRelatedField(
        queryset=RefJenisPembangkit.objects.all(),
        slug_field='id_ref_jenis_pembangkit',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    tree_jaringan = serializers.IntegerField(default=None, allow_null=True)

    alamat = serializers.CharField(
        max_length=100, default=None, allow_blank=True, allow_null=True, required=False
    )
    coverage = serializers.CharField(
        max_length=100, default=None, allow_blank=True, allow_null=True ,required=False
    )
    kva = serializers.IntegerField(default=None, allow_null=True)
    phase = serializers.CharField(
        max_length=20, default=None, allow_blank=True, allow_null=True, required=False
    )
    lat = serializers.FloatField(default=None, allow_null=True)
    lon = serializers.FloatField(default=None, allow_null=True)
    status_listrik = serializers.IntegerField(default=1, allow_null=True)
    no_tiang = serializers.CharField(
        max_length=50, default=None, allow_blank=True, allow_null=True, required=False
    )
    jenis_jaringan = serializers.CharField(
        max_length=100, default=None, allow_blank=True, allow_null=True, required=False
    )
    status_penyulang = serializers.CharField(
        max_length=100, default=None, allow_blank=True, allow_null=True, required=False
    )

    tgl_entri = serializers.DateField(format="%Y-%m-%d", read_only=True)
    tgl_update = serializers.DateField(format="%Y-%m-%d", read_only=True)
    no_urut = serializers.IntegerField(default=None, required=False,allow_null=True)
    ufr = serializers.IntegerField(default=None, required=False,allow_null=True)



    # nama_jenis_lokasi = serializers.RelatedField(source='ref_jenis_lokasi', read_only=True)

    class Meta:
        model = RefLokasi
        fields = '__all__'


class UDRefLokasiSerializers(serializers.ModelSerializer):
    queryset = RefLokasi.objects.all()

    nama_lokasi = serializers.CharField(max_length=100)
    kode_lokasi = serializers.CharField(max_length=100, required=False, allow_blank=True, allow_null=True)
    jumlah_pelanggan = serializers.IntegerField(required=False, allow_null=True)
    jumlah_jurusan = serializers.IntegerField(required=False, allow_null=True)
    jenis_trafo = serializers.CharField(max_length=20, required=False, allow_blank=True, allow_null=True)
    fungsi_scada = serializers.CharField(max_length=20, allow_blank=True, allow_null=True, required=False)
    kapasitas = serializers.IntegerField(required=False, allow_null=True)
    sub_sistem = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, required=False)
    pemilik = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, required=False)
    status_trafo = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, required=False)
    i_max = serializers.IntegerField(required=False, allow_null=True)
    ratio_ct = serializers.IntegerField(required=False, allow_null=True)
    ratio_vt = serializers.IntegerField(required=False, allow_null=True)
    fk_meter_pembanding = serializers.IntegerField(required=False, allow_null=True)
    primer_tegangan_max = serializers.IntegerField(required=False, allow_null=True)
    primer_tegangan_min = serializers.IntegerField(required=False, allow_null=True)
    sekunder_tegangan_min = serializers.IntegerField(required=False, allow_null=True)
    sekunder_tegangan_max = serializers.IntegerField(required=False, allow_null=True)
    sinkron_data = serializers.CharField(max_length=50, allow_blank=True, allow_null=True, required=False)
    jenis_layanan = serializers.CharField(max_length=50, allow_blank=True, allow_null=True, required=False)
    id_i = serializers.IntegerField(required=False, allow_null=True)
    id_v = serializers.IntegerField(required=False, allow_null=True)
    id_p = serializers.IntegerField(required=False, allow_null=True)
    id_amr = serializers.IntegerField(required=False, allow_null=True)
    id_portal_ext = serializers.IntegerField(required=False, allow_null=True)
    url_webservice = serializers.CharField(max_length=255, allow_blank=True, allow_null=True, required=False)
    jenis_gi = serializers.CharField(max_length=50, allow_blank=True, allow_null=True, required=False)
    faktor_meter = serializers.IntegerField(required=False, allow_null=True)
    faktor_kali = serializers.IntegerField(required=False, allow_null=True)
    dcc = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, required=False) 
    def_pengukuran_teg_primer = serializers.DecimalField(max_digits=5, decimal_places=2,required=False) 
    def_pengukuran_teg_sekunder = serializers.DecimalField(max_digits=5, decimal_places=2,required=False) 
    def_nilai_cosq = serializers.DecimalField(max_digits=5, decimal_places=2,required=False)  

    id_penyulang = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_zone = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_section = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_segment = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    id_parent_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_jenis_lokasi = serializers.SlugRelatedField(
        queryset=RefJenisLokasi.objects.all(),
        slug_field='id_ref_jenis_lokasi',
        allow_null=True,
        style={'base_template': 'input.html'}
    )
    # id_user_entri = serializers.SlugRelatedField(
    #     queryset=Users.objects.all(),
    #     slug_field='id_user',
    #     allow_null=True,
    #     style={'base_template': 'input.html'}
    # )
    # id_user_entri = serializers.ReadOnlyField()
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )

    id_uid = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_up3_1 = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_up3_2 = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ulp_1 = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ulp_2 = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_up2b = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    id_unit_pembangkit = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    id_pembangkit = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    id_gardu_induk = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    id_trafo_gi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    id_gardu_distribusi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    id_trafo_gd = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    id_gardu_hubung = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_province = serializers.SlugRelatedField(
        queryset=RefProvince.objects.all(),
        slug_field='id_ref_province',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_regency = serializers.SlugRelatedField(
        queryset=RefRegency.objects.all(),
        slug_field='id_ref_regency',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_district = serializers.SlugRelatedField(
        queryset=RefDistrict.objects.all(),
        slug_field='id_ref_district',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_jenis_pembangkit = serializers.SlugRelatedField(
        queryset=RefJenisPembangkit.objects.all(),
        slug_field='id_ref_jenis_pembangkit',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    tree_jaringan = serializers.IntegerField(required=False, allow_null=True)

    alamat = serializers.CharField(
        max_length=100, required=False, allow_blank=True, allow_null=True
    )
    coverage = serializers.CharField(
        max_length=100, required=False, allow_blank=True, allow_null=True
    )
    kva = serializers.IntegerField(required=False, allow_null=True)
    phase = serializers.CharField(
        max_length=20, required=False, allow_blank=True, allow_null=True 
    )
    lat = serializers.FloatField(required=False,allow_null=True)
    lon = serializers.FloatField(required=False,allow_null=True)
    status_listrik = serializers.IntegerField(required=False)
    no_tiang = serializers.CharField(
        max_length=50, required=False, allow_blank=True, allow_null=True 
    )
    jenis_jaringan = serializers.CharField(
        max_length=100, allow_blank=True, allow_null=True, required=False
    )
    status_penyulang = serializers.CharField(
        max_length=100, required=False, allow_blank=True, allow_null=True
    )
    no_urut = serializers.IntegerField(default=None, required=False,allow_null=True)
    ufr = serializers.IntegerField(default=None, required=False,allow_null=True)

    class Meta:
        model = RefLokasi
        fields = '__all__'


class RefLokasiSerializerTemp(serializers.ModelSerializer):
    ref_jenis_lokasi = RefJenisLokasierializer(read_only=True, source='id_ref_jenis_lokasi')
    parent_lokasi = IDSRef_LokasiSerializer(read_only=True, source='id_parent_lokasi')
    uid = IDSRef_LokasiSerializer(read_only=True, source='id_uid')
    up3_1 = IDSRef_LokasiSerializer(read_only=True,  source='id_up3_1')
    up3_2 = IDSRef_LokasiSerializer(read_only=True,  source='id_up3_2')
    ulp_1 = IDSRef_LokasiSerializer(read_only=True, source='id_ulp_1')
    ulp_2 = IDSRef_LokasiSerializer(read_only=True, source='id_ulp_2')
    penyulang = IDSRef_LokasiSerializer(read_only=True,  source='id_penyulang')
    section = IDSRef_LokasiSerializer(read_only=True,  source='id_section')
    segment = IDSRef_LokasiSerializer(read_only=True,  source='id_segment')
    zone = IDSRef_LokasiSerializer(read_only=True,  source='id_zone')
    unit_pembangkit = IDSRef_LokasiSerializer(read_only=True,  source='id_unit_pembangkit')
    pembangkit = IDSRef_LokasiSerializer(read_only=True,  source='id_pembangkit')
    gardu_induk = IDSRef_LokasiSerializer(read_only=True,  source='id_gardu_induk')
    trafo_gi = IDSRef_LokasiSerializer(read_only=True,  source='id_trafo_gi')
    gardu_distribusi = IDSRef_LokasiSerializer(read_only=True,  source='id_gardu_distribusi')
    trafo_gd = IDSRef_LokasiSerializer(read_only=True,  source='id_trafo_gd')
    gardu_hubung = IDSRef_LokasiSerializer(read_only=True, source='id_gardu_hubung') 

    # count_gardu = serializers.SerializerMethodField(source='children_temp')
    # children  = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = RefLokasiTemp
        fields = '__all__'
 

class UnitPembangkitSerializer(serializers.ModelSerializer):
    ref_jenis_lokasi = RefJenisLokasierializer(read_only=True, source='id_ref_jenis_lokasi')
    parent_lokasi = IDSRef_LokasiSerializer(read_only=True, source='id_parent_lokasi')
    uid = IDSRef_LokasiSerializer(read_only=True, source='id_uid')
    up3_1 = IDSRef_LokasiSerializer(read_only=True,  source='id_up3_1')
    up3_2 = IDSRef_LokasiSerializer(read_only=True,  source='id_up3_2')
    ulp_1 = IDSRef_LokasiSerializer(read_only=True,  source='id_ulp_1')
    ulp_2 = IDSRef_LokasiSerializer(read_only=True,  source='id_ulp_2')

    class Meta:
        model = RefLokasi
        fields = ['id_parent_lokasi', 'id_ref_jenis_lokasi', 'id_uid', 'id_up3_1', 'id_up3_2',  'id_ulp_1','id_ulp_2',
                  'nama_lokasi', 'kode_lokasi', 'alamat', 'tree_jaringan', 'lat', 'lon',
                  'tgl_entri', 'tgl_update', 'id_user_entri', 'id_user_update', 'status_listrik'
                  ]


class PembangkitSerializer(serializers.ModelSerializer):
    ref_jenis_lokasi = RefJenisLokasierializer(read_only=True, source='id_ref_jenis_lokasi')
    parent_lokasi = IDSRef_LokasiSerializer(read_only=True, source='id_parent_lokasi')
    uid = IDSRef_LokasiSerializer(read_only=True, source='id_uid')
    up3_1 = IDSRef_LokasiSerializer(read_only=True,  source='id_up3_1')
    up3_2 = IDSRef_LokasiSerializer(read_only=True,  source='id_up3_2')
    ulp_1 = IDSRef_LokasiSerializer(read_only=True,  source='id_ulp_1')
    ulp_2 = IDSRef_LokasiSerializer(read_only=True,  source='id_ulp_2')


    class Meta:
        model = RefLokasi
        fields = ['id_parent_lokasi', 'id_ref_jenis_lokasi', 'id_uid', 'id_up3_1', 'id_up3_2', 'id_ulp_1','id_ulp_2',
                  'nama_lokasi', 'kode_lokasi', 'alamat', 'tree_jaringan', 'lat', 'lon', 'kva', 'coverage', 'phase',
                  'no_tiang',
                  'tgl_entri', 'tgl_update', 'id_user_entri', 'id_user_update', 'status_listrik'
                  ]


class GISerializer(serializers.ModelSerializer):
    ref_jenis_lokasi = RefJenisLokasierializer(read_only=True, source='id_ref_jenis_lokasi')
    parent_lokasi = IDSRef_LokasiSerializer(read_only=True, source='id_parent_lokasi')
    uid = IDSRef_LokasiSerializer(read_only=True, source='id_uid')
    up3_1 = IDSRef_LokasiSerializer(read_only=True,  source='id_up3_1')
    up3_2 = IDSRef_LokasiSerializer(read_only=True,  source='id_up3_2')
    ulp_1 = IDSRef_LokasiSerializer(read_only=True,  source='id_ulp_1')
    ulp_2 = IDSRef_LokasiSerializer(read_only=True,  source='id_ulp_2')

    class Meta:
        model = RefLokasi
        fields = ['id_parent_lokasi', 'id_ref_jenis_lokasi', 'id_uid', 'id_up3_1', 'id_up3_2', 'id_ulp_1','id_ulp_2',
                  'nama_lokasi', 'kode_lokasi', 'alamat', 'tree_jaringan', 'lat', 'lon',
                  'tgl_entri', 'tgl_update', 'id_user_entri', 'id_user_update', 'status_listrik'
                  ]