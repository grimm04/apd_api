from django.db import models
from apps.users.models import Users
from apps.master.wilayah.ref_province.models import RefProvince

# Create your models here.
class RefRegency(models.Model):
    id_ref_regency = models.AutoField(primary_key=True, db_column='id_ref_regency')
    name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 

    id_ref_province = models.ForeignKey(
        RefProvince, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='provinces',
        db_column='id_ref_province'
    )
    class Meta:
        managed = False
        db_table = 'ref_regencies'

    def __str__(self):
        return self.id_ref_regency

 