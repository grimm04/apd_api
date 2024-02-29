
from django.db import models

class HistoriRC(models.Model):
    id_his_rc = models.IntegerField(default=None, blank=True, null=True)
    path1 = models.CharField(max_length=100, default=None, blank=True, null=True)
    path2 = models.CharField(max_length=100, default=None, blank=True, null=True)
    path3 = models.CharField(max_length=100, default=None, blank=True, null=True)
    path4 = models.CharField(max_length=100, default=None, blank=True, null=True)
    path5 = models.CharField(max_length=100, default=None, blank=True, null=True)
    b1 = models.CharField(max_length=100, default=None, blank=True, null=True)
    b2 = models.CharField(max_length=100, default=None, blank=True, null=True)
    b3 = models.CharField(max_length=100, default=None, blank=True, null=True)
    elem = models.CharField(max_length=100, default=None, blank=True, null=True)
    info = models.CharField(max_length=100, default=None, blank=True, null=True)
    datum_1 = models.CharField(max_length=100, default=None, blank=True, null=True)
    datum_2 = models.CharField(max_length=100, default=None, blank=True, null=True)
    status_1 = models.CharField(max_length=100, default=None, blank=True, null=True)
    status_2 = models.CharField(max_length=100, default=None, blank=True, null=True)
    msg_operator = models.CharField(max_length=100, default=None, blank=True, null=True)
    cek_remote = models.IntegerField(default=None, blank=True, null=True)
    durasi = models.CharField(max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return self.id_his_rc

EXPORT_HEADERS = []
EXPORT_FIELDS = []
EXPORT_RELATION_FIELD = []  