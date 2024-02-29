from django.db import models
from apps.apkt.apkt_trans_jar.models import APKTTransJAR

EXPORT_HEADERS = ['id_apkt_trans_log', 'tgl_mulai', 'tgl_selesai', 'input_apkt', 'output_apkt', 'tgl_buat', 'server_apkt', 'webservice', 'id_apkt_trans_jar']
EXPORT_FIELDS = ['id_apkt_trans_log', 'tgl_mulai', 'tgl_selesai', 'input_apkt', 'output_apkt', 'tgl_buat', 'server_apkt', 'webservice', 'id_apkt_trans_jar']
EXPORT_RELATION_FIELD = []

class APKTTransLog(models.Model):
    id_apkt_trans_log = models.AutoField(primary_key=True)
    tgl_mulai = models.DateTimeField(default=None, blank=True, null=True)
    tgl_selesai = models.DateTimeField(default=None, blank=True, null=True)
    input_apkt = models.CharField(max_length=4000, db_collation='SQL_Latin1_General_CP1_CI_AS')
    output_apkt = models.CharField(max_length=4000, db_collation='SQL_Latin1_General_CP1_CI_AS')
    tgl_buat = models.DateTimeField(default=None, blank=True, null=True)
    server_apkt = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    webservice = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    id_apkt_trans_jar = models.ForeignKey(
        APKTTransJAR, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_apkt_trans_jar'
    )

    class Meta:
        managed = True
        db_table = 'apkt_trans_log'

    def __str__(self):
        return self.id_apkt_trans_log