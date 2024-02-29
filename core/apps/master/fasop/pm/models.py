from django.db import models
from apps.master.jaringan.ref_lokasi.models import RefLokasi

class FASOPPM(models.Model):
    id_sch_pm = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status = models.IntegerField(default=0)
    nilai = models.IntegerField()
    tgl_aktif = models.DateField(auto_now_add=True, blank=True, null=True)
    tgl_berikut = models.DateField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sch_pm'

    def __str__(self):
        return self.id_sch_pm  

EXPORT_HEADERS = ['id_sch_pm', 'nama', 'bot','nilai','status']
EXPORT_FIELDS = ['id_sch_pm','nama', 'bot_name','nilai', 'status']
EXPORT_RELATION_FIELD = [] 