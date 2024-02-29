from django.db import models

EXPORT_HEADERS = ['id_apkt_trans_jar', 'no_laporan', 'nama_laporan', 'tgl_laporan', 'no_apkt', 'status_laporan', 'jenis_laporan', 'jlh_gardu_nyala', 'jlh_gardu_padam', 'tgl_nyala_terakhir', 'tgl_close_laporan', 'status_apkt_kirim_padam', 'tgl_padam', 'server_apkt', 'res_apkt_kirim_padam', 'id_feeder', 'feeder', 'status_data', 'tgl_nyala_awal', 'tgl_mulai_apkt_kirim_padam', 'tgl_selesai_apkt_kirim_padam', 'status_apkt_kirim_nyala', 'tgl_mulai_apkt_kirim_nyala', 'tgl_selesai_apkt_kirim_nyala', 'nama_switch', 'point_number_switch', 'kode_aset', 'jenis_aset', 'parent_aset', 'res_apkt_kirim_nyala', 'tgl_apkt_kirim_nyala']
EXPORT_FIELDS = ['id_apkt_trans_jar', 'no_laporan', 'nama_laporan', 'tgl_laporan', 'no_apkt', 'status_laporan', 'jenis_laporan', 'jlh_gardu_nyala', 'jlh_gardu_padam', 'tgl_nyala_terakhir', 'tgl_close_laporan', 'status_apkt_kirim_padam', 'tgl_padam', 'server_apkt', 'res_apkt_kirim_padam', 'id_feeder', 'feeder', 'status_data', 'tgl_nyala_awal', 'tgl_mulai_apkt_kirim_padam', 'tgl_selesai_apkt_kirim_padam', 'status_apkt_kirim_nyala', 'tgl_mulai_apkt_kirim_nyala', 'tgl_selesai_apkt_kirim_nyala', 'nama_switch', 'point_number_switch', 'kode_aset', 'jenis_aset', 'parent_aset', 'res_apkt_kirim_nyala', 'tgl_apkt_kirim_nyala']
EXPORT_RELATION_FIELD = []

class APKTTransJAR(models.Model):
    id_apkt_trans_jar = models.AutoField(primary_key=True)
    no_laporan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    nama_laporan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    tgl_laporan = models.DateTimeField(default=None, blank=True, null=True)
    no_apkt = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status_laporan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    jenis_laporan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    jlh_gardu_nyala = models.IntegerField(default=None, blank=True, null=True)
    jlh_gardu_padam = models.IntegerField(default=None, blank=True, null=True)
    tgl_nyala_terakhir = models.DateTimeField(default=None, blank=True, null=True)
    tgl_close_laporan = models.DateTimeField(default=None, blank=True, null=True)
    status_apkt_kirim_padam = models.IntegerField(default=None, blank=True, null=True)
    tgl_padam = models.DateTimeField(default=None, blank=True, null=True)
    server_apkt = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    res_apkt_kirim_padam = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    id_feeder = models.IntegerField(default=None, blank=True, null=True)
    feeder = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status_data = models.IntegerField(default=None, blank=True, null=True)
    tgl_nyala_awal = models.DateTimeField(default=None, blank=True, null=True)
    tgl_mulai_apkt_kirim_padam = models.DateTimeField(default=None, blank=True, null=True)
    tgl_selesai_apkt_kirim_padam = models.DateTimeField(default=None, blank=True, null=True)
    status_apkt_kirim_nyala = models.IntegerField(default=None, blank=True, null=True)
    tgl_mulai_apkt_kirim_nyala = models.DateTimeField(default=None, blank=True, null=True)
    tgl_selesai_apkt_kirim_nyala = models.DateTimeField(default=None, blank=True, null=True)
    nama_switch = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    point_number_switch = models.IntegerField(default=None, blank=True, null=True)
    kode_aset = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    jenis_aset = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    parent_aset = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    tgl_apkt_kirim_nyala = models.DateTimeField(default=None, blank=True, null=True)
    res_apkt_kirim_nyala = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = True
        db_table = 'apkt_trans_jar'

    def __str__(self):
        return self.id_apkt_trans_jar