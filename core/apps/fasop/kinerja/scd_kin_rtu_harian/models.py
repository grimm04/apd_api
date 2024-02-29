 
from django.db import models 
from apps.master.fasop.rtu.models import RTU



class ChildRTU(models.Model):

    
    up = models.IntegerField(default=None, blank=True, null=True)
    down = models.IntegerField(default=None, blank=True, null=True)
    downtime = models.IntegerField(default=None, blank=True, null=True)
    uptime = models.IntegerField(default=None, blank=True, null=True)
    performance = models.IntegerField(default=None, blank=True, null=True)
    faktor = models.IntegerField(default=None, blank=True, null=True)
    alltime = models.IntegerField(default=None, blank=True, null=True)
    kinerja = models.IntegerField(default=None, blank=True, null=True)

    datum = models.DateTimeField(auto_now_add=True, blank=True, null=True) 
    datum_created = models.DateTimeField(auto_now_add=True, blank=True, null=True) 
    point_number = models.IntegerField(default=None, blank=True, null=True)
    altime = models.IntegerField(default=None, blank=True, null=True)
    kinerja = models.IntegerField(default=None, blank=True, null=True)
    path3text = models.CharField(max_length=100)
    pointtypename = models.CharField(max_length=100)
    durasi = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
           return self.pointtypename
 

class SCD_KIN_RTU_HARIAN(models.Model):
        
    nama_pointtype = models.CharField(max_length=100, default=None, blank=True, null=True)
    id_pointtype = models.CharField(max_length=100, default=None, blank=True, null=True)
    child = models.ManyToManyField(ChildRTU, related_name='child')

    def __str__(self):
        return self.id_pointtype 


EXPORT_HEADERS = ['id_kin_rtu_harian', 'up','down', 'downtime','uptime','performance','faktor','alltime']
EXPORT_FIELDS = ['id_kin_rtu_harian', 'up','down', 'downtime','uptime','performance','faktor','alltime']
EXPORT_RELATION_FIELD = [] 