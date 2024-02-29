from django.db import models
from apps.opsisdis.jadwal_pemeliharaan.trans_jadwal_har.models import TransJadwalHar
class TransJadwalHarDok(models.Model):
    id_trans_jadwal_har_dok = models.AutoField(primary_key=True) 
    id_trans_jadwal_har = models.ForeignKey(
        TransJadwalHar, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_trans_jadwal_har'
    ) 
    file_name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    nama_dok = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jenis_dok = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_jadwal_har_dok'