from django.db import models 


# Create your models here.
class RefEpCuaca(models.Model):
    id_ref_ep_cuaca = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ref_ep_cuaca'
        
    def __str__(self):
        return self.id_ref_ep_cuaca

EXPORT_HEADERS = ['id_ref_ep_cuaca', 'nama']
EXPORT_FIELDS = ['id_ref_ep_cuaca', 'nama']
EXPORT_RELATION_FIELD = [] 