from django.db import models
from apps.tests.multi_insert.trans_rekap_padam.models import TransRekapPadam 

class TransRekapPadamSection(models.Model):
    id_trans_rekap_padam_section = models.BigAutoField(primary_key=True)
    id_trans_rekap_padam = models.ForeignKey(
        TransRekapPadam, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_trans_rekap_padam',
        related_name='trans_rekap_section'
    ) 
    section = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    beban_masuk = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    jam_masuk = models.DateTimeField(blank=True, null=True)
    inputer = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    inputer_at = models.DateTimeField(blank=True, null=True)
    beban_sebelum = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    jam_sebelum = models.DateTimeField(blank=True, null=True)
    durasi = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ens = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_rekap_padam_section'
        
    def __str__(self):
        return self.id_trans_rekap_padam_section