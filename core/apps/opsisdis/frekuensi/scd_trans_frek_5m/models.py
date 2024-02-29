from django.db import models

class Frekuensi5M(models.Model):
    id_meter = models.IntegerField(default=0, primary_key=True)
    value_2 = models.IntegerField(default=0)
    statusdata_2 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    datum_2 = models.DateTimeField(default=None, blank=True, null=True)
    datum_created = models.DateTimeField(default=None, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'scd_trans_frek_5m'

    def __str__(self):
        return self.id_meter