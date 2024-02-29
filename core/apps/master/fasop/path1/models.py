from django.db import models
from apps.master.jaringan.ref_lokasi.models import RefLokasi


class FASOPPATH1(models.Model):
    id = models.AutoField(primary_key=True)
    path1 = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status = models.IntegerField(default=0)
    # datum_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    id_lokasi = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_lokasi'
    )

    class Meta:
        managed = True
        db_table = 'scd_path1'

    def __str__(self):
        return self.id 

EXPORT_HEADERS = ['id', 'path1','lokasi', 'status']
EXPORT_FIELDS = ['id', 'path1', 'nama_lokasi', 'status']
EXPORT_RELATION_FIELD = [
            {'ref_lokasi':['nama_lokasi']}, 
        ] 