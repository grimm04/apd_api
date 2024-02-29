
from django.db import models

class KinerjaPeralatanScd(models.Model):
    id_kin_scd = models.IntegerField(default=None, blank=True, null=True)
    peralatan_scd = models.CharField(max_length=100, default=None, blank=True, null=True)
    path1text = models.CharField(max_length=100, default=None, blank=True, null=True)
    path2text = models.CharField(max_length=100, default=None, blank=True, null=True)
    path3text = models.CharField(max_length=100, default=None, blank=True, null=True)
    down = models.CharField(max_length=100, default=None, blank=True, null=True)
    downtime = models.CharField(max_length=100, default=None, blank=True, null=True)
    durasi = models.CharField(max_length=100, default=None, blank=True, null=True)
    avability = models.CharField(max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return self.id_kin_scd

EXPORT_HEADERS = []
EXPORT_FIELDS = []
EXPORT_RELATION_FIELD = []  