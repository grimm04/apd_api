from rest_framework import serializers
from .models import APKTTransJARDet
from apps.apkt.apkt_trans_jar.models import APKTTransJAR
from apps.users.models import Users
from apps.master.jaringan.ref_lokasi.models import RefLokasi

class SubAPKTTransJARSerializer(serializers.ModelSerializer):

    class Meta:
        model = APKTTransJAR
        fields = '__all__'

class SubUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['fullname', 'nip', 'gender']

class SubRefLokasiSerializer(serializers.ModelSerializer):

    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi', 'nama_lokasi', 'kode_lokasi', 'id_parent_lokasi']

class SubRefParentLokasiSerializer(serializers.ModelSerializer):

    class Meta:
        model = RefLokasi
        fields = '__all__'

class APKTTransJARDetSerializers(serializers.ModelSerializer):
    id_apkt_trans_jar = serializers.SlugRelatedField(
        queryset=APKTTransJAR.objects.all(),
        slug_field='id_apkt_trans_jar',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_apkt_trans_jar = SubAPKTTransJARSerializer(read_only=True, source='id_apkt_trans_jar')
    tgl_padam = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_nyala = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_apkt_kirim_padam = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_padam_scada = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    status_apkt_kirim_padam = serializers.IntegerField(default=None, allow_null=True)
    status_data = serializers.IntegerField(default=None, allow_null=True)
    id_user_update_padam = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_user_update_padam = SubUsersSerializer(read_only=True, source='id_user_update_padam')
    tgl_user_update_padam = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    server_apkt = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    gardu_mjd = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    id_feeder = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    penyulang = SubRefLokasiSerializer(read_only=True, source='id_feeder')
    id_gi = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_lokasi = SubRefParentLokasiSerializer(read_only=True, source='id_gi')
    uid = SubRefLokasiSerializer(read_only=True, source='id_gi.id_uid')
    up3_1 = SubRefLokasiSerializer(read_only=True,  source='id_gi.id_up3_1')
    up3_2 = SubRefLokasiSerializer(read_only=True,  source='id_gi.id_up3_2')
    ulp_1 = SubRefLokasiSerializer(read_only=True, source='id_gi.id_ulp_1')
    ulp_2 = SubRefLokasiSerializer(read_only=True, source='id_gi.id_ulp_2')
    section = SubRefLokasiSerializer(read_only=True,  source='id_gi.id_section')
    segment = SubRefLokasiSerializer(read_only=True,  source='id_gi.id_segment')
    zone = SubRefLokasiSerializer(read_only=True,  source='id_gi.id_zone')
    unit_pembangkit = SubRefLokasiSerializer(read_only=True,  source='id_gi.id_unit_pembangkit')
    pembangkit = SubRefLokasiSerializer(read_only=True,  source='id_gi.id_pembangkit')
    trafo_gi = SubRefLokasiSerializer(read_only=True,  source='id_gi.id_trafo_gi')
    gardu_distribusi = SubRefLokasiSerializer(read_only=True,  source='id_gi.id_gardu_distribusi')
    trafo_gd = SubRefLokasiSerializer(read_only=True,  source='id_gi.id_trafo_gd')
    gardu_hubung = SubRefLokasiSerializer(read_only=True, source='id_gi.id_gardu_hubung')
    gardu_induk = SubRefLokasiSerializer(read_only=True, source='id_gi')
    tgl_apkt_kirim_nyala = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    status_apkt_kirim_nyala = serializers.IntegerField(default=None, allow_null=True)
    res_apkt_kirim_nyala = serializers.CharField(max_length=1000, default=None, allow_blank=True, allow_null=True)
    tgl_apkt_kirim = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    res_apkt_kirim = serializers.CharField(max_length=1000, default=None, allow_blank=True, allow_null=True)
    id_user_update_nyala = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_user_update_nyala = SubUsersSerializer(read_only=True, source='id_user_update_nyala')
    tgl_user_update_nyala = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_mulai_apkt_kirim_padam = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_selesai_apkt_kirim_padam = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_mulai_apkt_kirim_nyala = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_selesai_apkt_kirim_nyala = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    kode_aset = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    parent_aset = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    kode_ref_aset_jenis = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    kode_feeder = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    jenis_aset = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_user_update = SubUsersSerializer(read_only=True, source='id_user_update')
    tgl_user_update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    res_apkt_kirim_padam = serializers.CharField(max_length=1000, default=None, allow_blank=True, allow_null=True)

    class Meta:
        model = APKTTransJARDet
        fields = '__all__'

class UDAPKTTransJARDetSerializers(serializers.ModelSerializer):
    id_apkt_trans_jar = serializers.SlugRelatedField(
        queryset=APKTTransJAR.objects.all(),
        slug_field='id_apkt_trans_jar',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_apkt_trans_jar = SubAPKTTransJARSerializer(read_only=True, source='id_apkt_trans_jar')
    tgl_padam = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_nyala = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_apkt_kirim_padam = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_padam_scada = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    status_apkt_kirim_padam = serializers.IntegerField(default=None, allow_null=True)
    status_data = serializers.IntegerField(default=None, allow_null=True)
    id_user_update_padam = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_user_update_padam = SubUsersSerializer(read_only=True, source='id_user_update_padam')
    tgl_user_update_padam = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    server_apkt = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    gardu_mjd = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    id_feeder = serializers.IntegerField(default=None, allow_null=True)
    id_gi = serializers.IntegerField(default=None, allow_null=True)
    tgl_apkt_kirim_nyala = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    status_apkt_kirim_nyala = serializers.IntegerField(default=None, allow_null=True)
    res_apkt_kirim_nyala = serializers.CharField(max_length=1000, default=None, allow_blank=True, allow_null=True)
    tgl_apkt_kirim = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    res_apkt_kirim = serializers.CharField(max_length=1000, default=None, allow_blank=True, allow_null=True)
    id_user_update_nyala = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_user_update_nyala = SubUsersSerializer(read_only=True, source='id_user_update_nyala')
    tgl_user_update_nyala = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_mulai_apkt_kirim_padam = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_selesai_apkt_kirim_padam = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_mulai_apkt_kirim_nyala = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_selesai_apkt_kirim_nyala = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    kode_aset = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    parent_aset = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    kode_ref_aset_jenis = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    kode_feeder = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    jenis_aset = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_user_update = SubUsersSerializer(read_only=True, source='id_user_update')
    tgl_user_update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    res_apkt_kirim_padam = serializers.CharField(max_length=1000, default=None, allow_blank=True, allow_null=True)

    class Meta:
        model = APKTTransJARDet
        fields = '__all__'