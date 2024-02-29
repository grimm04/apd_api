 
from django.db import models 

class RealtimeScada(models.Model):
    point_number =models.IntegerField(default=None, blank=True, null=True)
    durasi = models.CharField(max_length=100, default=None, blank=True, null=True)
    tgl_gangguan = models.CharField(max_length=100, default=None, blank=True, null=True)
    value = models.IntegerField(default=None, blank=True, null=True)
    point_name = models.CharField(max_length=100, default=None, blank=True, null=True)
    jenis_point = models.CharField(max_length=100, default=None, blank=True, null=True)

    def __str__(self):
           return self.point_number

class PointtypeAnak(models.Model):
    id_pointtype = models.IntegerField(default=None, blank=True, null=True)
    id_pointtype_induk = models.IntegerField(default=None, blank=True, null=True)
    nama_pointtype = models.CharField(max_length=100, default=None, blank=True, null=True)
    jenis_pointtype = models.CharField(max_length=100, default=None, blank=True, null=True)
    jml_children = models.IntegerField(default=None, blank=True, null=True)
    children = models.ManyToManyField(RealtimeScada, related_name='children')

    def __str__(self):
        return self.id_pointtype 


class PointtypeInduk(models.Model):
    id_pointtype = models.IntegerField(default=None, blank=True, null=True)
    nama_pointtype = models.CharField(max_length=100, default=None, blank=True, null=True)
    jenis_pointtype = models.CharField(max_length=100, default=None, blank=True, null=True)
    id_pointtype_induk = models.IntegerField(default=None, blank=True, null=True)
    jml_pointtype = models.IntegerField(default=None, blank=True, null=True)
    anak_pointtype = models.ManyToManyField(PointtypeAnak, related_name='anak_pointtype')

    def __str__(self):
        return self.id_pointtype  


EXPORT_HEADERS = ['id_kin_rtu_harian', 'up','down', 'downtime','uptime','performance','faktor','alltime']
EXPORT_FIELDS = ['id_kin_rtu_harian', 'up','down', 'downtime','uptime','performance','faktor','alltime']
EXPORT_RELATION_FIELD = [] 