from django.db import models
from apps.users.models import Users
from apps.master.jaringan.ref_lokasi.models import RefLokasi 
from apps.master.opsisdis.rekap_padam.ref_ep_indikasi.models import RefEpIndikasi
from apps.master.opsisdis.rekap_padam.ref_ep_cuaca.models import RefEpCuaca
from apps.master.opsisdis.rekap_padam.ref_ep_penyebab_ggn.models import RefEpPenyebabGgn
from apps.master.opsisdis.rekap_padam.ref_ep_fdir.models import RefEpFdir
class TransEp(models.Model):
    id_trans_ep = models.BigAutoField(primary_key=True)
    no_event = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    no_apkt = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    tanggal = models.DateField(auto_now_add=True, blank=True, null=True)
    jam_padam = models.DateTimeField(blank=True, null=True)
    penyebab = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    beban_padam = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    indikasi = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    lbs_manual = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jenis_keypoint = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_keypoint = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_keypoint', related_name='trans_rekap_padam_keypoint'
    )  
    penyulang_gi = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    up3 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    ulp = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jlh_gardu_padam = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    pelanggan_tm = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    pelanggan_vip = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    wilayah_padam = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    cuaca = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    recloser = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    gardu_induk = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    r = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    s = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    t = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    n = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    jam_buka = models.DateTimeField(blank=True, null=True)
    jam_tutup = models.DateTimeField(blank=True, null=True)
    jam_trip = models.DateTimeField(blank=True, null=True)
    jam_normal = models.DateTimeField(blank=True, null=True)
    keterangan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    gardu_hubung = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jenis_padam = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jml_ggn_tahun = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jml_ggn_bulan = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    indikator_kerja = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    sectionalizer_kerja = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jam_wrc = models.DateTimeField(blank=True, null=True)
    jam_isolasi = models.DateTimeField(blank=True, null=True)
    jam_pengusutan = models.DateTimeField(blank=True, null=True)
    penyebab_ggn = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    jenis_pemeliharaan = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status_proteksi = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    sepatetik_trip = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    koordinasi_proteksi = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    gagal_ar = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    keterangan_proteksi = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    penyulang_fdir = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    keterangan_penyulang_fdir = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    fai_arus_ggn_hmi = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    fai_mtrz_hmi = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    keterangan_fai_mtrz_hmi = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    fai_fiohl_hmi = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    dispat_kalsel_1 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dispat_kalsel_2 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dispat_kalteng_1 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dispat_kalteng_2 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    keterangan_fai_fiohl_hmi = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    ens = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    kategori_ggn = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    keterangan_ggn = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status_penyulang_fdir = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status_fai_mtrz_hmi = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status_fai_fiohl_hmi = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    gangguan_ditemukan = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    motorized = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    posting = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    dispat_kalteng_3 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dispat_kalsel_3 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    aco_kerja = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    peralatan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    photo = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    id_ref_ep_indikasi = models.ForeignKey(
        RefEpIndikasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_ref_ep_indikasi', related_name='trans_rekap_padam_indikasi'
    )
    id_ref_ep_penyebab_ggn = models.ForeignKey(
        RefEpPenyebabGgn, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_ref_penyebab_ggn', related_name='trans_rekap_padam_penyebab_ggn'
    )
    id_ref_ep_cuaca = models.ForeignKey(
        RefEpCuaca, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_ref_ep_cuaca', related_name='trans_rekap_padam_cuaca'
    )
    id_up3 = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_up3', related_name='trans_rekap_padam_up3'
    )
    id_ulp = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_ulp', related_name='trans_rekap_padam_ulp'
    ) 
    id_penyulang_fdir = models.ForeignKey(
        RefEpFdir, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_penyulang_fdir', related_name='trans_rekap_padam_penyulang_fdir'
    ) 
    tgl_entri = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    tgl_update = models.DateTimeField(auto_now=True, blank=True, null=True) 
    id_user_entri = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_entri',
        db_column='id_user_entri'
    )
    id_user_update = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_update',
        db_column='id_user_update'
    )
 

    class Meta:
        managed = False
        db_table = 'trans_ep'
    
    def __str__(self):
        return self.id_trans_ep


EXPORT_HEADERS_TRANS_EP = ['NO','NO. EVENT','NO. APKT','TANGGAL PADAM','LBS MANUAL / FCO', 'MTRZ','RECLOSER',
                 'PENYULANG GH','GARDU HUBUNG','PENYULANG GI','GARDU INDUK','JAM BUKA','JAM TRIP','JAM TUTUP',
                 'BEBAN PADAM','INDIKASI','R','S','T','N','CUACA','ZONA TERGANGGU','UP3','ULP','WILAYAH PADAM','JUMLAH GARDU PADAM','KATEGORI GANGGUAN',
                 'PENYEBAB GANGGUAN','GANGGUAN DITEMUKAN','KETERANGAN','JENIS PEMELIHARAAN','PERALATAN RC','RC OPEN','RC CLOSE','STATUS OPEN','STATUS CLOSE','KOORDINASI PROTEKSI','KETERANGAN',
                 'SIMPATETIK TRIP','GAGAL AR','FAI ARUS GANGGUAN HMI','PENYULANG FDIR','STATUS PENYULANG FDIR','KETERANGAN FDIR','FAI MTRZ HMI','STATUS MTRZ HMI','FAI FIOHL HMI',
                 'STATUS FAI FIOHL HMI','FAULT INDIKATOR KERJA','SECTIONALYZER KERJA','ACO KERJA','JAM WRC','JAM ISOLASI','JAM PENGUSUTAN','JAM NORMAL','DISPATCHER DCC KALSEL 1','DISPATCHER DCC KALSEL 2',
                 'DISPATCHER DCC KALSEL 3','DISPATCHER DCC KALTENG 1','DISPATCHER DCC KALTENG 2','DISPATCHER DCC KALTENG 3','DURASI (MENIT)','ENS (kWh)','ENS (Rupiah)','Durasi WRC','Durasi Isolasi','Durasi Pengusutan','Durasi Perbaikan','Durasi Penormalan']
EXPORT_FIELDS = []
EXPORT_RELATION_FIELD = [ 
    {
        'up3': [
            'nama_up3', 
        ]
    }, 
    {
        'ref_jenis_pekerjaan': [
            'nama_jenis_pekerjaan', 
        ]
    }, 
    {
        'user_entri': [
            'fullname', 
        ]
    }, 
]
EXPORT_HEADERS_CAPTION = [{
    'row_start': 4,
    'header_row_start': 3,
    'data': [
        {'name': 'Laporan Jadwal Pemeliharaan', 'column': 'A1:J1', 'width': 15, 'merge': True,'align':'center','type':'row'},
        # {'name': 'Gardu Induk', 'column': 'A2:B2', 'width': 15, 'merge': True,'align':'left','type':'row'},
        # {'name': 'Penyulang', 'column': 'A3:B3', 'width': 15, 'merge': True,'align':'left','type':'row'},
        # # {'name': 'Area', 'column': 'A4:B4', 'width': 10, 'merge': True,'align':'left','type':'row'}, 
        # {'name': 'Tanggal', 'column': 'A4:B4', 'width': 10, 'merge': True,'align':'left','type':'row'}, 
        # {'name': 'nama_gardu_induk', 'relation':'ref_parent_lokasi', 'column': 'C2:C2', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
        # {'name': 'nama_lokasi','relation':'ref_lokasi', 'column': 'C3:C3', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
        # # {'name': 'nama_area','relation':'ref_lokasi', 'column': 'C4:C4', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
        # {'name': 'date_hari','relation':None, 'column': 'C4:C4', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
    ]
}]