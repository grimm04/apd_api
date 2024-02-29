
from email.policy import default
from rest_framework import serializers
from .models import TransRekapPadam
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from datetime import datetime

@extend_schema_serializer(
    exclude_fields=('id_trans_tm_pembangkit', 'tgl_entri', 'tgl_update'),
    examples=[
         OpenApiExample(
            'Example',
            summary='Example',
            description='Example',
            value= 
                {
                    "no_event": "string",
                    "no_apkt": "string",
                    "r": 0,
                    "s": 0,
                    "t": 0,
                    "n": 0,
                    "jam_padam": datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
                    "jam_tutup": datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
                    "jam_normal": datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                },
            request_only=True,
            response_only=False,
        ),
    ]
)
#Custom Validation Tanpa Model(params bebas)
class PostCustomNonModel(serializers.Serializer):
    no_event = serializers.CharField(allow_null=True,max_length=100, default=None, required=False)
    no_apkt = serializers.CharField(allow_null=True,max_length=100, default=None, required=False)
    r = serializers.DecimalField(allow_null=True,max_digits=8, decimal_places=2, required=False)
    s = serializers.DecimalField(allow_null=True,max_digits=8, decimal_places=2, required=False)
    t = serializers.DecimalField(allow_null=True,max_digits=8, decimal_places=2, required=False)
    n = serializers.DecimalField(allow_null=True,max_digits=8, decimal_places=2, required=False)  
    jam_padam = serializers.DateTimeField(allow_null=True, format="%Y-%m-%d %H:%M:%S.%f")
    jam_tutup = serializers.DateTimeField(allow_null=True, format="%Y-%m-%d %H:%M:%S.%f")
    jam_normal = serializers.DateTimeField(allow_null=True, format="%Y-%m-%d %H:%M:%S.%f")
    



# Serializer/Validasi Berdasarkan Model (pastikan (allow_null=True) jika dimasukan ke dalam params create)
class TransRekapSerializer(serializers.ModelSerializer): 
    no_event = serializers.CharField(allow_null=True,max_length=50, required=False)
    no_apkt = serializers.CharField(allow_null=True,max_length=50, required=False)
    tanggal = serializers.DateField(format="%Y-%m-%d", default=None, required=False,allow_null=True)
    jam_padam = serializers.DateTimeField(allow_null=True, format="%Y-%m-%d %H:%M:%S.%f",required=False)
    penyebab = serializers.CharField(allow_null=True,max_length=100, required=False)
    beban_padam = serializers.DecimalField(allow_null=True,max_digits=8, decimal_places=2, required=False)
    indikasi = serializers.CharField(allow_null=True,max_length=100, required=False)
    lbs_manual = serializers.CharField(allow_null=True,max_length=100, required=False)
    jenis_keypoint = serializers.CharField(allow_null=True,max_length=20, required=False)
    id_keypoint = serializers.IntegerField(allow_null=True,default=None, required=False)
    penyulang_gi = serializers.CharField(allow_null=True,max_length=100, required=False)
    up3 = serializers.CharField(allow_null=True,max_length=100, required=False)
    ulp = serializers.CharField(allow_null=True,max_length=100, required=False)
    jlh_gardu_padam = serializers.CharField(allow_null=True,max_length=20, required=False)
    pelanggan_tm = serializers.CharField(allow_null=True,max_length=20, required=False)
    pelanggan_vip = serializers.CharField(allow_null=True,max_length=20, required=False)
    wilayah_padam = serializers.CharField(allow_null=True,max_length=500, required=False)
    cuaca = serializers.CharField(allow_null=True,max_length=100, required=False)
    recloser = serializers.CharField(allow_null=True,max_length=100, required=False)
    gardu_induk = serializers.CharField(allow_null=True,max_length=100, required=False)
    r = serializers.DecimalField(allow_null=True,max_digits=8, decimal_places=2, required=False)
    s = serializers.DecimalField(allow_null=True,max_digits=8, decimal_places=2, required=False)
    t = serializers.DecimalField(allow_null=True,max_digits=8, decimal_places=2, required=False)
    n = serializers.DecimalField(allow_null=True,max_digits=8, decimal_places=2, required=False) 
    buka = serializers.DateTimeField(default=None,format="%Y-%m-%d %H:%M:%S.%f", allow_null=True, required=False)
    tutup = serializers.DateTimeField(allow_null=True, format="%Y-%m-%d %H:%M:%S.%f",required=False)
    trip = serializers.DateTimeField(allow_null=True, format="%Y-%m-%d %H:%M:%S.%f",required=False)
    normal = serializers.DateTimeField(allow_null=True, format="%Y-%m-%d %H:%M:%S.%f",required=False)
    keterangan = serializers.CharField(allow_null=True,max_length=100, required=False)
    gardu_hubung = serializers.CharField(allow_null=True,max_length=100, required=False)
    jenis_padam = serializers.CharField(allow_null=True,max_length=50, required=False)
    jml_ggn_tahun = serializers.CharField(allow_null=True,max_length=20, required=False)
    jml_ggn_bulan = serializers.CharField(allow_null=True,max_length=20, required=False)
    indikator_kerja = serializers.CharField(allow_null=True,max_length=100, required=False)
    sectionalizer_kerja = serializers.CharField(allow_null=True,max_length=100, required=False)
    jam_wrc = serializers.DateTimeField(allow_null=True, format="%Y-%m-%d %H:%M:%S.%f",required=False)
    jam_isolasi = serializers.DateTimeField(allow_null=True, format="%Y-%m-%d %H:%M:%S.%f",required=False)
    jam_pengusutan = serializers.DateTimeField(allow_null=True, format="%Y-%m-%d %H:%M:%S.%f",required=False)
    penyebab_ggn = serializers.DecimalField(allow_null=True,max_digits=20, decimal_places=0, required=False)
    jenis_pemeliharaan = serializers.CharField(allow_null=True,max_length=20, required=False)
    status_proteksi = serializers.CharField(allow_null=True,max_length=50, required=False)
    sepatetik_trip = serializers.CharField(allow_null=True,max_length=100, required=False)
    koordinasi_proteksi = serializers.CharField(allow_null=True,max_length=100, required=False)
    gagal_ar = serializers.CharField(allow_null=True,max_length=100, required=False)
    keterangan_proteksi = serializers.CharField(allow_null=True,max_length=500, required=False)
    penyulang_fdir = serializers.DecimalField(allow_null=True,max_digits=18, decimal_places=0, required=False)
    keterangan_penyulang_fdir = serializers.CharField(allow_null=True,max_length=100, required=False)
    fai_arus_ggn_hmi = serializers.CharField(allow_null=True,max_length=100, required=False)
    fai_mtrz_hmi = serializers.DecimalField(allow_null=True,max_digits=18, decimal_places=0, required=False)
    keterangan_fai_mtrz_hmi = serializers.CharField(allow_null=True,max_length=500, required=False)
    fai_fiohl_hmi = serializers.DecimalField(allow_null=True,max_digits=18, decimal_places=0, required=False)
    dispat_kalsel_1 = serializers.CharField(allow_null=True,max_length=100, required=False)
    dispat_kalsel_2 = serializers.CharField(allow_null=True,max_length=100, required=False)
    dispat_kalteng_1 = serializers.CharField(allow_null=True,max_length=100, required=False)
    dispat_kalteng_2 = serializers.CharField(allow_null=True,max_length=100, required=False)
    keterangan_fai_fiohl_hmi = serializers.CharField(allow_null=True,max_length=500, required=False)
    jam_normal = serializers.DateTimeField(allow_null=True, format="%Y-%m-%d %H:%M:%S.%f",required=False)
    ens = serializers.DecimalField(allow_null=True,max_digits=8, decimal_places=2, required=False)
    kategori_ggn = serializers.CharField(allow_null=True,max_length=100, required=False)
    keterangan_ggn = serializers.CharField(allow_null=True,max_length=500, required=False)
    status_penyulang_fdir = serializers.CharField(allow_null=True,max_length=50, required=False)
    status_fai_mtrz_hmi = serializers.CharField(allow_null=True,max_length=50, required=False)
    status_fai_fiohl_hmi = serializers.CharField(allow_null=True,max_length=50, required=False)
    gangguan_ditemukan = serializers.CharField(allow_null=True,max_length=20, required=False)
    id_trans_rekap_padam_section = serializers.IntegerField(allow_null=True,default=None, required=False)
    motorized = serializers.CharField(allow_null=True,max_length=100, required=False)
    posting = serializers.DecimalField(allow_null=True,max_digits=18, decimal_places=0, required=False)
    dispat_kalteng_3 = serializers.CharField(allow_null=True,max_length=100, required=False)
    dispat_kalsel_3 = serializers.CharField(allow_null=True,max_length=100, required=False)
    id_trans_rekap_padam_peralatan = serializers.IntegerField(allow_null=True,default=None, required=False)
    aco_kerja = serializers.CharField(allow_null=True,max_length=20, required=False)
    peralatan = serializers.CharField(allow_null=True,max_length=100, required=False)
    photo = serializers.CharField(allow_null=True,max_length=100, required=False)
    lat = serializers.FloatField(allow_null=True,default=None, required=False)
    lon = serializers.FloatField(allow_null=True,default=None, required=False)
    id_up3 = serializers.IntegerField(allow_null=True,default=None, required=False)
    id_ulp = serializers.IntegerField(allow_null=True,default=None, required=False)

    class Meta:
        model   = TransRekapPadam
        fields  = '__all__'