from django.db import models 
from apps.master.opsisdis.pm.ref_pm_detail.models import RefPMDetail


# Create your models here.
class RefPMDetailLogic(models.Model): 
    id_ref_pm_detail_logic = models.AutoField(primary_key=True, db_column='id_ref_pm_detail_logic')
    nilai_range = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  
    kesimpulan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  

    id_ref_pm_detail = models.ForeignKey(
        RefPMDetail, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_ref_pm_detail'
    ) 

    class Meta:
        managed = False
        db_table = 'ref_pm_detail_logic'

    def __str__(self):
        return self.id_ref_pm_detail_logic