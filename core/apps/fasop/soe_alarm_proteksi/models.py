from statistics import mode
from django.db import models

class SoeAlarmProteksi(models.Model):
    id_kin_digital_harian = models.IntegerField(default=None, blank=True, null=True)
    tanggal = models.CharField(max_length=100, default=None, blank=True, null=True)
    path1text = models.CharField(max_length=100, default=None, blank=True, null=True)
    path2text = models.CharField(max_length=100, default=None, blank=True, null=True)
    path3text = models.CharField(max_length=100, default=None, blank=True, null=True)
    path4text = models.CharField(max_length=100, default=None, blank=True, null=True)
    path5text = models.CharField(max_length=100, default=None, blank=True, null=True)
    point_text = models.CharField(max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return self.id_kin_digital_harian

class PathText(models.Model):
    path_text = models.CharField(max_length=100, default=None, blank=True, null=True)
    def __str__(self):
        return self.path_text

EXPORT_HEADERS = []
EXPORT_FIELDS = []
EXPORT_RELATION_FIELD = []  