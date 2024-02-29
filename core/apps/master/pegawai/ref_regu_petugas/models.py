from django.db import models


# Create your models here.
class REF_REGU_PETUGAS_MODELS(models.Model):
    id_ref_regu_petugas = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'ref_regu_petugas'

    def __str__(self):
        return self.id_ref_regu_petugas
        
EXPORT_HEADERS = ['id_ref_regu_petugas', 'name']
EXPORT_FIELDS = ['id_ref_regu_petugas','name']
EXPORT_RELATION_FIELD =  []