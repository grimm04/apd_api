from django.db import models


# Create your models here.
class Departemen(models.Model):
    id_departemen = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'ref_departemen'

    def __str__(self):
        return self.id_departemen

EXPORT_HEADERS = ['id_departemen', 'nama']
EXPORT_FIELDS = ['id_departemen','nama']
EXPORT_RELATION_FIELD =  []