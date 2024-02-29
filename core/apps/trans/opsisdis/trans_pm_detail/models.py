from django.db import models
import datetime
from apps.users.models import Users  
from apps.master.opsisdis.pm.ref_pm.models import RefPM 
from apps.trans.opsisdis.trans_pm.models import TransPM

# Create your models here.
class TransPMDetail(models.Model): 
    id_trans_pm_detail = models.AutoField(primary_key=True, db_column='id_trans_pm_detail')  
    # status = models.IntegerField(default=None,blank=True, null=True) 
    nama = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    nilai_acuan = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    nilai_pemeriksaan = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    satuan = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    kesimpulan = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    id_trans_pm = models.ForeignKey(
        TransPM, on_delete=models.CASCADE, default=None, blank=True, null=True,
        db_column='id_trans_pm'
    )
    id_ref_pm = models.ForeignKey(
        RefPM, on_delete=models.CASCADE, default=None, blank=True, null=True,  related_name='trans_pm_detail_ref_pm',
        db_column='id_ref_pm'
    ) 
    id_induk_ref_pm_detail = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, 
        db_column='id_induk_ref_pm_detail'
    )
    induk = models.ForeignKey(
        RefPM, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='ref_pmInduk',
        db_column='induk'
    ) 

    #default
    id_user_entri = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, 
        db_column='id_user_entri'
    )
    id_user_update = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_update',
        db_column='id_user_update'
    ) 
    tgl_entri = models.DateField(auto_now_add=True, blank=True, null=True)
    tgl_update = models.DateField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_pm_detail'

    def __str__(self):
        return self.id_trans_pm_detail