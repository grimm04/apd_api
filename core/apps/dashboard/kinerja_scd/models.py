from django.db import models

class DashboardKinerjaScdBoxBulanan(models.Model):
    pointtype = models.CharField(max_length=100, default=None, blank=True, null=True)
    nilai_bulanan = models.FloatField(default=None, blank=True, null=True)

    def __str__(self):
        return self.pointtype

class DashboardKinerjaScdBoxKomulatif(models.Model):
    pointtype = models.CharField(max_length=100, default=None, blank=True, null=True)
    nilai_komulatif = models.FloatField(default=None, blank=True, null=True)

    def __str__(self):
        return self.pointtype

class DashboardKinerjaScdBoxRTU(models.Model):
    pointtype = models.CharField(max_length=100, default=None, blank=True, null=True)
    jml = models.FloatField(default=None, blank=True, null=True)

    def __str__(self):
        return self.pointtype

class DashboardKinerjaScdGrafik(models.Model):
    pointtype = models.CharField(max_length=100, default=None, blank=True, null=True)
    target = models.FloatField(default=None, blank=True, null=True)
    real_bulanan = models.FloatField(default=None, blank=True, null=True)
    real_komulatif = models.FloatField(default=None, blank=True, null=True)

    def __str__(self):
        return self.pointtype

class DashboardKinerjaScdRTUOutOffPool(models.Model):
    peralatan = models.CharField(max_length=100, default=None, blank=True, null=True)
    durasi = models.CharField(max_length=100, default=None, blank=True, null=True)
    lat = models.CharField(max_length=100, default=None, blank=True, null=True)
    lon = models.CharField(max_length=100, default=None, blank=True, null=True)
   
    def __str__(self):
        return self.peralatan


EXPORT_HEADERS = []
EXPORT_FIELDS = []
EXPORT_RELATION_FIELD = []  