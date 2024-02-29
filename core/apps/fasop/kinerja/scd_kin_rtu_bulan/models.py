 
from django.db import models 
from apps.master.fasop.rtu.models import RTU


class SCD_KIN_RTU_BULAN(models.Model):
    id_kin_rtu_bulan = models.AutoField(primary_key=True)  
    up = models.IntegerField(default=None, blank=True, null=True)
    down = models.IntegerField(default=None, blank=True, null=True)
    downtime = models.IntegerField(default=None, blank=True, null=True)
    uptime = models.IntegerField(default=None, blank=True, null=True)
    performance = models.IntegerField(default=None, blank=True, null=True)
    faktor = models.IntegerField(default=None, blank=True, null=True)
    alltime = models.IntegerField(default=None, blank=True, null=True)
    kinerja = models.IntegerField(default=None, blank=True, null=True)
    point_number = models.ForeignKey(
        RTU, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='point_number'
    )

    datum = models.DateTimeField(default=None, blank=True, null=True) 
    datum_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)  
    class Meta:
        managed = True
        db_table = 'scd_kin_rtu_bulan'

    def __str__(self):
        return self.id_kin_rtu_bulan 

EXPORT_HEADERS = ['id_kin_rtu_bulan', 'up','down', 'downtime','uptime','performance','faktor']
EXPORT_FIELDS = ['id_kin_rtu_bulan', 'up','down', 'downtime','uptime','performance','faktor']
EXPORT_RELATION_FIELD = [] 