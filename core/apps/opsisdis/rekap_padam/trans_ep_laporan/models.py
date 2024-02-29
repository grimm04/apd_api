from django.db import models
from apps.opsisdis.rekap_padam.trans_ep.models import TransEp 


class TransEpLaporan(models.Model):
    id_trans_ep_laporan = models.BigAutoField(primary_key=True)
    id_trans_ep = models.ForeignKey(
        TransEp, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_trans_ep'
    )  
    tegangan = models.CharField(max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    piket = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    peralatan = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jam_buka = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jam_tutup = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    arus_gangguan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    resume = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    eksekusi_rc = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    eksekusi_mc = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status_s = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status_g = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_ep_laporan'
    

    def __str__(self):
        return self.id_trans_ep_laporan
