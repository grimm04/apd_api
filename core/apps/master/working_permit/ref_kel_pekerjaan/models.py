from django.db import models

class RefKelPekerjaan(models.Model):
    id_ref_kel_pekerjaan = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    alias = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    kategori = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS') 

    class Meta:
        managed = True
        db_table = 'ref_kel_pekerjaan'

    def __str__(self):
        return self.id_ref_kel_pekerjaan

EXPORT_HEADERS = ['id_ref_kel_pekerjaan', 'name','kategori']
EXPORT_FIELDS = ['id_ref_kel_pekerjaan', 'name','kategori']
EXPORT_RELATION_FIELD = [] 