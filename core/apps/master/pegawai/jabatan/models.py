from django.db import models


# Create your models here.
class Jabatan(models.Model):
    id_jabatan = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'ref_jabatan'

    def __str__(self):
        return self.id_jabatan
        
EXPORT_HEADERS = ['id_jabatan', 'nama']
EXPORT_FIELDS = ['id_jabatan','nama']
EXPORT_RELATION_FIELD =  []