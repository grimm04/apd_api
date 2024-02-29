from django.db import models
from apps.master.opsisdis.frekuensi.models import Frekuensi

class FrekuensiRTL(models.Model):
    id_frek_rtl = models.AutoField(primary_key=True)
    id_meter = models.ForeignKey(
        Frekuensi, on_delete=models.CASCADE, db_column='id_meter'
    )
    value_1 = models.FloatField(default=0)
    datum_1 = models.DateTimeField(default=None, blank=True, null=True)
    value_2 = models.FloatField(default=0)
    datum_2 = models.DateTimeField(default=None, blank=True, null=True)
    statusdata_1 = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    statusdata_2 = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    statusdevice_1 = models.BinaryField(max_length=50)
    datum_created = models.DateTimeField(default=None, blank=True, null=True)
    datum_updated = models.DateTimeField(default=None, blank=True, null=True)
    min_value = models.FloatField(default=0)
    min_datum = models.DateTimeField(default=None, blank=True, null=True)
    max_value = models.FloatField(default=0)
    max_datum = models.DateTimeField(default=None, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'scd_frek_rtl'

    def __str__(self):
        return self.id_meter