from django.db import models
from apps.users.models import Users 
from apps.master.jaringan.ref_lokasi.models import RefLokasi 
from apps.master.opsisdis.ref_jenis_pekerjaan.models import RefJenisPekerjaan
from apps.master.pegawai.perusahaan.models import Perusahaan



class TransJadwalHar(models.Model):
    id_trans_jadwal_har = models.AutoField(primary_key=True) 
    id_ref_jenis_pekerjaan = models.ForeignKey(
        RefJenisPekerjaan, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_ref_jenis_pekerjaan'
    ) 
    id_gardu_induk = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_gardu_induk', related_name='tranf_opsisdis_gi'
    )
    gardu_induk = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) 
    id_penyulang = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_penyulang', related_name='tranf_opsisdis_penyulang'
    )
    penyulang = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) 
    id_gardu = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_gardu', related_name='tranf_opsisdis_gardu'
    )
    gardu = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) 
    id_up3 = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_up3', related_name='tranf_opsisdis_up3'
    )
    up3 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_lama = models.IntegerField(blank=True, null=True)
    nomor = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jam_pekerjaan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jam_buka = models.DateTimeField(blank=True, null=True)
    jam_tutup = models.DateTimeField(blank=True, null=True)
    jam_normal = models.DateTimeField(blank=True, null=True) 
    pelaksana_pek = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) 
    sifat_jenis_pek = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    butuh_padam = models.IntegerField(blank=True, null=True)
    jtm = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    keterangan = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jenis_jadwal = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    usulan_dari = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jenis_pelayanan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    wilayah = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    wilayah_padam = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    tgl = models.DateField(blank=True, null=True)
    periode = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    tgl_periode = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status_pekerjaan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    approval_area1 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    approval_apd1 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    respon_apd = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    sat_ker = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    tgl_progres = models.DateField(blank=True, null=True)

    id_pelaksana = models.ForeignKey(
        Perusahaan, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='har_peklaksana',
        db_column='id_pelaksana'
    )
    id_pengawas = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='har_pengawas',
        db_column='id_pengawas'
    )

    id_user_entri = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_entri',
        db_column='id_user_entri'
    )
    id_user_update = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_update',
        db_column='id_user_update'
    )
    tgl_entri = models.DateField(auto_now_add=True, blank=True, null=True)
    tgl_update = models.DateField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_jadwal_har'

    
    def __str__(self):
        return self.id_trans_jadwal_har

EXPORT_HEADERS = ['Tanggal','Nomor','Jam Pekerjaan','Gardu Induk','Penyulang', 'Gardu','Up3', 'Jenis Pekerjaan','Jenis Pelayanan','Status Pekerjaan','Pembuat']
EXPORT_FIELDS = ['tgl','nomor', 'jam_pekerjaan', 'nama_gardu_induk','nama_penyulang', 'nama_gardu','nama_up3','nama_jenis_pekerjaan','jenis_pelayanan','status_pekerjaan','fullname']
EXPORT_RELATION_FIELD = [
    {
        'gardu_induk': [
            'nama_gardu_induk', 
        ]
    }, 
    {
        'penyulang': [
            'nama_penyulang', 
        ]
    }, 
    {
        'gardu': [
            'nama_gardu', 
        ]
    }, 
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