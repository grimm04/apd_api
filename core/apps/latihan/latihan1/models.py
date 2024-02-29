from django.db import models 
from apps.users.models import Users

class LATIHAN(models.Model):
    id_latihan = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')   
    class Meta:
        managed = True
        db_table = 'latihan'

    def __str__(self):
        return self.id_latihan
 