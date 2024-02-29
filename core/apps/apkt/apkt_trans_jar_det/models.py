from django.db import models
from apps.apkt.apkt_trans_jar.models import APKTTransJAR
from apps.users.models import Users
from apps.master.jaringan.ref_lokasi.models import RefLokasi

EXPORT_HEADERS = ['id_apkt_trans_jar_det', 'tgl_padam', 'tgl_nyala', 'tgl_apkt_kirim_padam', 'tgl_padam_scada', 'status_apkt_kirim_padam', 'status_data', 'id_user_update_padam', 'tgl_user_update_padam', 'server_apkt', 'gardu_mjd', 'id_feeder', 'id_gi', 'tgl_apkt_kirim_nyala', 'status_apkt_kirim_nyala', 'res_apkt_kirim_nyala', 'tgl_apkt_kirim', 'res_apkt_kirim', 'id_user_update_nyala', 'tgl_user_update_nyala', 'tgl_mulai_apkt_kirim_padam', 'tgl_selesai_apkt_kirim_padam', 'tgl_mulai_apkt_kirim_nyala', 'tgl_selesai_apkt_kirim_nyala', 'kode_aset', 'parent_aset', 'kode_ref_aset_jenis', 'kode_feeder', 'jenis_aset', 'id_user_update', 'tgl_user_update', 'res_apkt_kirim_padam']
EXPORT_FIELDS = ['id_apkt_trans_jar_det', 'tgl_padam', 'tgl_nyala', 'tgl_apkt_kirim_padam', 'tgl_padam_scada', 'status_apkt_kirim_padam', 'status_data', 'id_user_update_padam', 'tgl_user_update_padam', 'server_apkt', 'gardu_mjd', 'id_feeder', 'id_gi', 'tgl_apkt_kirim_nyala', 'status_apkt_kirim_nyala', 'res_apkt_kirim_nyala', 'tgl_apkt_kirim', 'res_apkt_kirim', 'id_user_update_nyala', 'tgl_user_update_nyala', 'tgl_mulai_apkt_kirim_padam', 'tgl_selesai_apkt_kirim_padam', 'tgl_mulai_apkt_kirim_nyala', 'tgl_selesai_apkt_kirim_nyala', 'kode_aset', 'parent_aset', 'kode_ref_aset_jenis', 'kode_feeder', 'jenis_aset', 'id_user_update', 'tgl_user_update', 'res_apkt_kirim_padam']
EXPORT_RELATION_FIELD = []

class APKTTransJARDet(models.Model):
    id_apkt_trans_jar_det = models.AutoField(primary_key=True)
    id_apkt_trans_jar = models.ForeignKey(
        APKTTransJAR, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_apkt_trans_jar'
    )
    tgl_padam = models.DateTimeField(default=None, blank=True, null=True)
    tgl_nyala = models.DateTimeField(default=None, blank=True, null=True)
    tgl_apkt_kirim_padam = models.DateTimeField(default=None, blank=True, null=True)
    tgl_padam_scada = models.DateTimeField(default=None, blank=True, null=True)
    status_apkt_kirim_padam = models.IntegerField(default=None, blank=True, null=True)
    status_data = models.IntegerField(default=None, blank=True, null=True)
    id_user_update_padam = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_update_padam',
        db_column='id_user_update_padam'
    )
    tgl_user_update_padam = models.DateTimeField(default=None, blank=True, null=True)
    server_apkt = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    gardu_mjd = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    id_feeder = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_feeder',
        related_name='%(class)s_id_feeder'
    )
    id_gi = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_gi',
        related_name='%(class)s_id_gi'
    )
    tgl_apkt_kirim_nyala = models.DateTimeField(default=None, blank=True, null=True)
    status_apkt_kirim_nyala = models.IntegerField(default=None, blank=True, null=True)
    res_apkt_kirim_nyala = models.CharField(max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS')
    tgl_apkt_kirim = models.DateTimeField(default=None, blank=True, null=True)
    res_apkt_kirim = models.CharField(max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS')
    id_user_update_nyala = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_update_nyala',
        db_column='id_user_update_nyala'
    )
    tgl_user_update_nyala = models.DateTimeField(default=None, blank=True, null=True)
    tgl_mulai_apkt_kirim_padam = models.DateTimeField(default=None, blank=True, null=True)
    tgl_selesai_apkt_kirim_padam = models.DateTimeField(default=None, blank=True, null=True)
    tgl_mulai_apkt_kirim_nyala = models.DateTimeField(default=None, blank=True, null=True)
    tgl_selesai_apkt_kirim_nyala = models.DateTimeField(default=None, blank=True, null=True)
    kode_aset = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    parent_aset = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    kode_ref_aset_jenis = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    kode_feeder = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    jenis_aset = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    id_user_update = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_update',
        db_column='id_user_update'
    )
    tgl_user_update = models.DateTimeField(default=None, blank=True, null=True)
    res_apkt_kirim_padam = models.CharField(max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = True
        db_table = 'apkt_trans_jar_det'

    def __str__(self):
        return self.id_apkt_trans_jar_det