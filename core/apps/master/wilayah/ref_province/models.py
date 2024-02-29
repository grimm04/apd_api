from django.db import models
from apps.users.models import Users


# Create your models here.
class RefProvince(models.Model):
    id_ref_province = models.AutoField(primary_key=True, db_column='id_ref_province')
    name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 

    class Meta:
        managed = False
        db_table = 'ref_provinces'

    def __str__(self):
        return self.id_ref_province

 