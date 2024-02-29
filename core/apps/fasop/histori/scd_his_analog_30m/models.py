 
from django.db import models 
from apps.master.fasop.c_point.models import CPoint

class SCD_ANALOG_HIS_30M(models.Model):
    id = models.AutoField(primary_key=True) 
    point_number = models.ForeignKey(
        CPoint, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='point_number'
    ) 
    value_2 = models.IntegerField(default=None, blank=True, null=True) 
    datum = models.DateTimeField(default=None, blank=True, null=True)  
    datum_created = models.DateTimeField(auto_now_add=True, blank=True, null=True) 

    status_2 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  
    class Meta:
        managed = True
        db_table = 'scd_analog_his_30m'

    def __str__(self):
        return self.id 

EXPORT_HEADERS = ['id', 'Jenis_Point','b1', 'b2','b3','tanggal_awal','datum', 'status_2', 'value_2']
EXPORT_FIELDS = ['id', 'point_type', 'path2text', 'path3text','path4text','datum','status_2','value_2']
EXPORT_RELATION_FIELD = [
            {'c_point':['point_name','point_type','path2text','path3text','path4text']}, 
        ] 