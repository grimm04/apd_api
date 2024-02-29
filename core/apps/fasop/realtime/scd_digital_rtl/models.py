 
from django.db import models 
from apps.master.fasop.c_point.models import CPoint

class SCD_DIGITAL_RTL(models.Model):
    id = models.AutoField(primary_key=True) 
    point_number = models.ForeignKey(
        CPoint, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='point_number',related_name='digital'
    )
    status = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status_1 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status_2 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  
    statekey_1 = models.FloatField(default=None, blank=True, null=True)
    statekey_2 = models.FloatField(default=None, blank=True, null=True)
    datum = models.DateTimeField(default=None, blank=True, null=True)
    datum_1 = models.DateTimeField(default=None, blank=True, null=True)
    datum_2 = models.DateTimeField(default=None, blank=True, null=True) 
    datum_capture = models.DateTimeField(default=None, blank=True, null=True) 
    datum_created = models.DateTimeField(auto_now_add=True, blank=True, null=True) 

    kesimpulan = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    value = models.FloatField(default=None, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'scd_digital_rtl'

    def __str__(self):
        return self.id 

EXPORT_HEADERS = ['id', 'Jenis_Point','b1', 'b2','b3','tanggal_awal','msec_awal', 'status_awal', 'tanggal_akhir','msec_akhir','status_akhir','durasi','kesimpulan']
EXPORT_FIELDS = ['id', 'point_type', 'path1text', 'path2text','path3text','datum_1','statekey_1','status_1','datum_2','statekey_2','status_2','datum_capture','datum','kesimpulan']
EXPORT_RELATION_FIELD = [
            {'c_point':['point_name','point_type','path1text','path2text','path3text','path4text']}, 
        ] 