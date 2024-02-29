from numpy import source
from rest_framework import serializers

from apps.users.models import Users
from .models import RefAset
from apps.master.aset.ref_aset_status.models import RefAsetStatus
from apps.master.aset.ref_aset_jenis.models import RefAsetJenis
from apps.master.aset.ref_aset_manufaktur.models import RefAsetManufaktur
from apps.master.aset.ref_aset_level.models import RefAsetLevel
from apps.master.aset.ref_aset_lantai.models import RefAsetLantai
from apps.master.aset.ref_aset_ruangan.models import RefAsetRuangan
from apps.master.aset.ref_aset_kondisi.models import RefAsetKondisi
from apps.master.aset.ref_aset_rak.models import RefAsetRak
from apps.master.jaringan.ref_lokasi.models import RefLokasi


class SubRefAsetParentSerializer(serializers.ModelSerializer):
    nama_parent = serializers.CharField(source='nama')
    class Meta:
        model = RefAset
        fields = ['id_ref_aset_parent', 'nama','nama_parent']


class SubRefAsetStatusSerializer(serializers.ModelSerializer):
    nama_status = serializers.CharField(source='nama') 
    class Meta:
        model = RefAsetStatus
        fields = ['id_ref_aset_status', 'nama', 'status','nama_status']


class SubRefAsetJenisSerializer(serializers.ModelSerializer): 
    class Meta:
        model = RefAsetJenis
        fields = ['id_ref_aset_jenis', 'nama_aset_jenis', 'status', 'tree_jaringan']


class SubRefAsetManufakturSerializer(serializers.ModelSerializer):
    nama_manufaktur = serializers.CharField(source='nama') 
    class Meta:
        model = RefAsetManufaktur
        fields = ['id_ref_aset_manufaktur', 'nama', 'status','nama_manufaktur']


class SubRefAsetLevelSerializer(serializers.ModelSerializer):
    nama_level = serializers.CharField(source='nama')  
    class Meta:
        model = RefAsetLevel
        fields = ['id_ref_aset_level', 'nama', 'status','nama_level']


class SubRefAsetLantaiSerializer(serializers.ModelSerializer):
    nama_lantai = serializers.CharField(source='nama')  
    class Meta:
        model = RefAsetLantai
        fields = ['id_ref_aset_lantai', 'nama', 'status','nama_lantai']


class SubRefAsetRuanganSerializer(serializers.ModelSerializer):
    nama_ruangan = serializers.CharField(source='nama')  
    class Meta:
        model = RefAsetRuangan
        fields = ['id_ref_aset_ruangan', 'nama', 'status','nama_ruangan']


class SubRefAsetKondisiSerializer(serializers.ModelSerializer):
    nama_kondisi = serializers.CharField(source='nama') 

    class Meta:
        model = RefAsetKondisi
        fields = ['id_ref_kondisi_aset', 'nama', 'status','nama_kondisi']


class SubRefAsetRakSerializer(serializers.ModelSerializer):
    nama_rak = serializers.CharField(source='nama') 

    class Meta:
        model = RefAsetRak
        fields = ['id_ref_aset_rak', 'nama', 'status','nama_rak']


class SubRefLokasi1Serializer(serializers.ModelSerializer): 
    nama_lokasi_1 = serializers.CharField(source='nama_lokasi') 

    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi', 'nama_lokasi', 'kode_lokasi','nama_lokasi_1']
class SubRefLokasi2Serializer(serializers.ModelSerializer): 
    nama_lokasi_2 = serializers.CharField(source='nama_lokasi') 

    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi', 'nama_lokasi', 'kode_lokasi','nama_lokasi_2']
class SubRefLokasi3Serializer(serializers.ModelSerializer): 
    nama_lokasi_3 = serializers.CharField(source='nama_lokasi') 

    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi', 'nama_lokasi', 'kode_lokasi','nama_lokasi_3']
class SubRefLokasi4Serializer(serializers.ModelSerializer): 
    nama_lokasi_4 = serializers.CharField(source='nama_lokasi')  
    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi', 'nama_lokasi', 'kode_lokasi','nama_lokasi_4']


class RefAsetSerializersList(serializers.ModelSerializer):
    ref_aset_parent = SubRefAsetParentSerializer(read_only=True, source='id_ref_aset_parent') 
    ref_aset_status = SubRefAsetStatusSerializer(read_only=True, source='id_ref_aset_status') 
    ref_aset_jenis = SubRefAsetJenisSerializer(read_only=True, source='id_ref_aset_jenis')
    ref_aset_manufaktur = SubRefAsetManufakturSerializer(read_only=True, source='id_ref_aset_manufaktur')
    ref_aset_level = SubRefAsetLevelSerializer(read_only=True, source='id_ref_aset_level')
    ref_lokasi_1 = SubRefLokasi1Serializer(read_only=True, source='id_ref_lokasi_1')
    ref_lokasi_2 = SubRefLokasi2Serializer(read_only=True, source='id_ref_lokasi_2')
    ref_lokasi_3 = SubRefLokasi3Serializer(read_only=True, source='id_ref_lokasi_3')
    ref_lokasi_4 = SubRefLokasi4Serializer(read_only=True, source='id_ref_lokasi_4')
    ref_aset_lantai = SubRefAsetLantaiSerializer(read_only=True, source='id_ref_aset_lantai')
    ref_aset_ruangan = SubRefAsetRuanganSerializer(read_only=True, source='id_ref_aset_ruangan')
    ref_aset_kondisi = SubRefAsetKondisiSerializer(read_only=True, source='id_ref_aset_kondisi')
    ref_aset_rak = SubRefAsetRakSerializer(read_only=True, source='id_ref_aset_rak')

    class Meta:
        model = RefAset
        fields = '__all__'


class CRRefAsetSerializers(serializers.ModelSerializer):
    id_ref_aset_parent = serializers.SlugRelatedField(
        queryset=RefAset.objects.all(),
        slug_field='id_ref_aset',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    jenis_aset = serializers.CharField(max_length=100)

    id_ref_aset_status = serializers.SlugRelatedField(
        queryset=RefAsetStatus.objects.all(),
        slug_field='id_ref_aset_status',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    id_ref_aset_jenis = serializers.SlugRelatedField(
        queryset=RefAsetJenis.objects.all(),
        slug_field='id_ref_aset_jenis',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    id_ref_aset_manufaktur = serializers.SlugRelatedField(
        queryset=RefAsetManufaktur.objects.all(),
        slug_field='id_ref_aset_manufaktur',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    id_ref_aset_level = serializers.SlugRelatedField(
        queryset=RefAsetLevel.objects.all(),
        slug_field='id_ref_aset_level',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    id_trans_pm = serializers.IntegerField(default=None, allow_null=True)
    id_aset_mutasi = serializers.IntegerField(default=None, allow_null=True)

    id_ref_lokasi_1 = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    id_ref_lokasi_2 = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    id_ref_lokasi_3 = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 
    id_ref_lokasi_4 = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    tgl_buat = serializers.DateField(format="%Y-%m-%d", read_only=True)
    tgl_update = serializers.DateField(format="%Y-%m-%d", read_only=True)

    no_aset_internal = serializers.IntegerField(default=None, allow_null=True)
    no_aset_external = serializers.IntegerField(default=None, allow_null=True)
    nama = serializers.CharField(max_length=100)
    no_seri = serializers.CharField(max_length=100)
    model = serializers.CharField(max_length=100)
    tipe = serializers.CharField(max_length=100)
    tahun = serializers.IntegerField(default=None, allow_null=True)
    dimensi_lebar = serializers.IntegerField(default=None, allow_null=True)
    dimensi_panjang = serializers.IntegerField(default=None, allow_null=True)
    dimensi_tinggi = serializers.IntegerField(default=None, allow_null=True)
    dimensi_satuan = serializers.IntegerField(default=None, allow_null=True)
    massa_berat = serializers.IntegerField(default=None, allow_null=True)
    massa_satuan = serializers.IntegerField(default=None, allow_null=True)

    id_ref_aset_lantai = serializers.SlugRelatedField(
        queryset=RefAsetLantai.objects.all(),
        slug_field='id_ref_aset_lantai',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    id_ref_aset_ruangan = serializers.SlugRelatedField(
        queryset=RefAsetRuangan.objects.all(),
        slug_field='id_ref_aset_ruangan',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    id_ref_aset_kondisi = serializers.SlugRelatedField(
        queryset=RefAsetKondisi.objects.all(),
        slug_field='id_ref_kondisi_aset',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    id_ref_aset_rak = serializers.SlugRelatedField(
        queryset=RefAsetRak.objects.all(),
        slug_field='id_ref_aset_rak',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    class Meta:
        model = RefAset
        fields = '__all__'


class UDRefAsetSerializers(serializers.ModelSerializer):
    queryset = RefAset.objects.all()

    id_ref_aset_parent = serializers.SlugRelatedField(
        queryset=RefAset.objects.all(),
        slug_field='id_ref_aset',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    jenis_aset = serializers.CharField(max_length=100)

    id_ref_aset_status = serializers.SlugRelatedField(
        queryset=RefAsetStatus.objects.all(),
        slug_field='id_ref_aset_status',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_aset_jenis = serializers.SlugRelatedField(
        queryset=RefAsetJenis.objects.all(),
        slug_field='id_ref_aset_jenis',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_aset_manufaktur = serializers.SlugRelatedField(
        queryset=RefAsetManufaktur.objects.all(),
        slug_field='id_ref_aset_manufaktur',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_aset_level = serializers.SlugRelatedField(
        queryset=RefAsetLevel.objects.all(),
        slug_field='id_ref_aset_level',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    id_trans_pm = serializers.IntegerField(default=None, allow_null=True)
    id_aset_mutasi = serializers.IntegerField(default=None, allow_null=True)

    id_ref_lokasi_1 = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_lokasi_2 = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_lokasi_3 = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_lokasi_4 = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    tgl_buat = serializers.DateField(format="%Y-%m-%d", read_only=True)
    tgl_update = serializers.DateField(format="%Y-%m-%d", read_only=True)

    no_aset_internal = serializers.IntegerField(default=None, allow_null=True)
    no_aset_external = serializers.IntegerField(default=None, allow_null=True)
    nama = serializers.CharField(max_length=100)
    no_seri = serializers.CharField(max_length=100)
    model = serializers.CharField(max_length=100)
    tipe = serializers.CharField(max_length=100)
    tahun = serializers.IntegerField(default=None, allow_null=True)
    dimensi_lebar = serializers.IntegerField(default=None, allow_null=True)
    dimensi_panjang = serializers.IntegerField(default=None, allow_null=True)
    dimensi_tinggi = serializers.IntegerField(default=None, allow_null=True)
    dimensi_satuan = serializers.IntegerField(default=None, allow_null=True)
    massa_berat = serializers.IntegerField(default=None, allow_null=True)
    massa_satuan = serializers.IntegerField(default=None, allow_null=True)

    id_ref_aset_lantai = serializers.SlugRelatedField(
        queryset=RefAsetLantai.objects.all(),
        slug_field='id_ref_aset_lantai',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_aset_ruangan = serializers.SlugRelatedField(
        queryset=RefAsetRuangan.objects.all(),
        slug_field='id_ref_aset_ruangan',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_aset_kondisi = serializers.SlugRelatedField(
        queryset=RefAsetKondisi.objects.all(),
        slug_field='id_ref_kondisi_aset',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_aset_rak = serializers.SlugRelatedField(
        queryset=RefAsetRak.objects.all(),
        slug_field='id_ref_aset_rak',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    class Meta:
        model = RefAset
        fields = '__all__'