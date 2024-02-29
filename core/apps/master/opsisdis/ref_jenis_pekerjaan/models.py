from django.db import models 

class RefJenisPekerjaan(models.Model):
    id_ref_jenis_pekerjaan = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ref_jenis_pekerjaan'

    def __str__(self):
        return self.id_ref_jenis_pekerjaan