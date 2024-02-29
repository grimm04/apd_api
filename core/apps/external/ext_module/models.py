from django.db import models


# Create your models here.
class ExtModule(models.Model):
    id_module = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'ext_module'

    def __str__(self):
        return self.id_module
