from django.db import models 
from apps.master.wilayah.ref_regency.models import RefRegency

# Create your models here.
class RefDistrict(models.Model):
    id_ref_district = models.AutoField(primary_key=True, db_column='id_ref_district')
    name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 

    id_ref_regency = models.ForeignKey(
        RefRegency, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='regencies',
        db_column='id_ref_regency'
    )
    class Meta:
        managed = False
        db_table = 'ref_districts'

    def __str__(self):
        return self.id_ref_district

 