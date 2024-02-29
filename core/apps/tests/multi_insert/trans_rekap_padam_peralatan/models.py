from django.db import models
from apps.tests.multi_insert.trans_rekap_padam.models import TransRekapPadam

class TransRekapPadamPeralatan(models.Model):
    id_trans_rekap_padam_peralatan = models.BigAutoField(primary_key=True)
    id_trans_rekap_padam = models.ForeignKey(
        TransRekapPadam, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_trans_rekap_padam',
        related_name='trans_rekap_peralatan'
    ) 
    peralatan_rc = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    rc_open = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    rc_close = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status_rc_open = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status_rc_close = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    inputer = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    inputer_at = models.DateTimeField(blank=True, null=True)
    updater_at = models.DateTimeField(blank=True, null=True)
    tgl = models.DateTimeField(blank=True, null=True)
    id_peralatan = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_rekap_padam_peralatan'

    def __str__(self):
        return self.id_trans_rekap_padam_peralatan