
from django.db import models

class HistoriPeralatanScd(models.Model):
    id_his_scd = models.IntegerField(default=None, blank=True, null=True)
    peralatan_scd = models.CharField(max_length=100, default=None, blank=True, null=True)
    path1 = models.CharField(max_length=100, default=None, blank=True, null=True)
    path2 = models.CharField(max_length=100, default=None, blank=True, null=True)
    path3 = models.CharField(max_length=100, default=None, blank=True, null=True)
    tanggal_awal = models.CharField(max_length=100, default=None, blank=True, null=True)
    status_awal = models.CharField(max_length=100, default=None, blank=True, null=True)
    tanggal_akhir = models.CharField(max_length=100, default=None, blank=True, null=True)
    status_akhir = models.CharField(max_length=100, default=None, blank=True, null=True)
    durasi = models.CharField(max_length=100, default=None, blank=True, null=True)
    kesimpulan = models.CharField(max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return self.id_his_scd

EXPORT_HEADERS = []
EXPORT_FIELDS = []
EXPORT_RELATION_FIELD = []  