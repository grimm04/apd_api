from django.db import models

from apps.master.opsisdis.jenis_penyebab_gangguan.models import JenisPenyebabGangguan


# Create your models here.
class PenyebabGangguan(models.Model):
    id_penyebab_gangguan = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    id_jenis_penyebab_gangguan = models.ForeignKey(
        JenisPenyebabGangguan, on_delete=models.CASCADE, default=None, blank=True, null=True,
        related_name='%(class)s_jenis_penyebab_gangguan', db_column='id_jenis_penyebab_gangguan'
    )

    class Meta:
        managed = False
        db_table = 'ref_penyebab_gangguan'

    def __str__(self):
        return self.id_penyebab_gangguan

EXPORT_HEADERS = ['id_penyebab_gangguan', 'nama','Jenis']
EXPORT_FIELDS = ['id_penyebab_gangguan','nama','nama_jenis']
EXPORT_RELATION_FIELD =  [
    {'id_jenis_penyebab_gangguan':['nama_jenis']},  
]