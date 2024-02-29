from django.db import models 


# Create your models here.
class RefPemilikJaringan(models.Model):
    id_pemilik = models.AutoField(primary_key=True, db_column='id_pemilik')
    nama = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    status = models.IntegerField(default=None, null=True,blank=True)
    class Meta:
        managed = False
        db_table = 'ref_pemilik_jaringan'

    def __str__(self):
        return self.id_pemilik

EXPORT_HEADERS = ['id_pemilik', 'nama']
EXPORT_FIELDS = ['id_pemilik', 'nama']
EXPORT_RELATION_FIELD = [] 