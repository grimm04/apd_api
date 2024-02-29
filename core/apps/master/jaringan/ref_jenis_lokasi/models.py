from django.db import models
from apps.users.models import Users


# Create your models here.
class RefJenisLokasi(models.Model):
    id_ref_jenis_lokasi = models.AutoField(primary_key=True, db_column='id_ref_jenis_lokasi')
    nama_jenis_lokasi = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    id_user_entri = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_entri',
        db_column='id_user_entri'
    )
    id_user_update = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_update',
        db_column='id_user_update'
    )
    tgl_entri = models.DateField(auto_now_add=True, blank=True, null=True)
    tgl_update = models.DateField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ref_jenis_lokasi'

    def __str__(self):
        return self.id_ref_jenis_lokasi

 