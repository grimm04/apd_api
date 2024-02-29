from django.db import models

# Create your models here.
class Perusahaan(models.Model):
    id_perusahaan = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    nama_direktur = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    alamat_kantor = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    no_hp = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')

    tgl_entri = models.DateField(auto_now_add=True, blank=True, null=True)
    tgl_update = models.DateField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ref_perusahaan'

    def __str__(self):
        return self.id_perusahaan

EXPORT_HEADERS = ['id_perusahaan', 'nama']
EXPORT_FIELDS = ['id_perusahaan','nama']
EXPORT_RELATION_FIELD =  []