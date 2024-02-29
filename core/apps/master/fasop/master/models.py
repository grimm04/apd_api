from django.db import models
from apps.master.jaringan.ref_lokasi.models import RefLokasi
from apps.master.fasop.point_type.models import PointType

class FASOPMASTER(models.Model):
    point_number = models.AutoField(primary_key=True)
    path3text = models.CharField(max_length=18, db_collation='SQL_Latin1_General_CP1_CI_AS')
    path3 = models.CharField(max_length=18, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status = models.IntegerField(blank=True, null=True)
    faktor = models.CharField(max_length=18, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    send_telegram = models.IntegerField(blank=True, null=True)
    kinerja = models.IntegerField(blank=True, null=True)
    id_pointtype = models.ForeignKey(
        PointType, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_pointtype', related_name='masters'
    )
    id_ref_lokasi = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_ref_lokasi'
    )

    class Meta:
        managed = True
        db_table = 'scd_ref_master'

    def __str__(self):
        return self.point_number

EXPORT_HEADERS = ['ID', 'station','nama', 'b3text','jenis_point','faktor','aktif','telegram','kinerja']
EXPORT_FIELDS = ['point_number','nama_lokasi', 'nama', 'b3text','nama_jenis', 'faktor','status','send_telegram','kinerja']
EXPORT_RELATION_FIELD = [
            {'ref_lokasi':['nama_lokasi']}, 
            {'pointtype':['nama_jenis']}, 
        ] 