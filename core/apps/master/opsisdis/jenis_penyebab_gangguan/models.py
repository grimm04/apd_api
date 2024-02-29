from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class JenisPenyebabGangguan(models.Model):
    id_jenis_penyebab_gangguan = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'ref_jenis_penyebab_gangguan'

    def __str__(self):
        return self.id_jenis_penyebab_gangguan
