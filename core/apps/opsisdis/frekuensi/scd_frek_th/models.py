from django.db import models
from apps.master.opsisdis.frekuensi.models import Frekuensi 

class FrekuensiTH(models.Model):
    id_frek_th = models.IntegerField(default=0, primary_key=True)
    id_meter = models.ForeignKey(
        Frekuensi, on_delete=models.CASCADE, db_column='id_meter'
    )
    datum = models.DateTimeField(default=None, blank=True, null=True)
    range_nilai = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    lokasi = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True)
    jumlah = models.IntegerField(default=0)
    datum_created = models.DateTimeField(default=None, blank=True, null=True)
    # id_ref_lokasi = models.ForeignKey(
    #     RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_ref_lokasi',
    #     related_name='%(class)s_id_ref_lokasi'
    # )

    class Meta:
        managed = True
        db_table = 'scd_frek_th'

    def __str__(self):
        return self.id_frek_th