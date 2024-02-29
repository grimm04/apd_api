from django.db import models
from apps.master.jaringan.ref_lokasi.models import RefLokasi


# Create your models here.
class RefLokasiGD(models.Model):
    id_ref_lokasi_gd = models.AutoField(primary_key=True, db_column='id_ref_lokasi_gd') 
    id_ref_lokasi = models.ForeignKey(
        RefLokasi, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_ref_lokasi',
        db_column='id_ref_lokasi'
    )  
    id_ref_lokasi_child = models.ForeignKey(
        RefLokasi, on_delete=models.CASCADE,
        default=None, blank=True, null=True, related_name='%(class)s_ref_lokasi_child',
        db_column='id_ref_lokasi_child'
    )  

    class Meta:
        managed = False
        db_table = 'ref_lokasi_gd'

    def __str__(self):
        return self.id_ref_lokasi_gd

 