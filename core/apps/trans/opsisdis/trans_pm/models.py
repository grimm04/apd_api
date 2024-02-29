from django.db import models
import datetime
from apps.users.models import Users 
from apps.master.opsisdis.pm.ref_hi.models import RefHI
from apps.master.opsisdis.pm.ref_pm.models import RefPM
from apps.master.aset.ref_aset.models import RefAset
from apps.trans.opsisdis.trans_aset_mutasi.models import TransAsetMutasi
from apps.trans.opsisdis.trans_wo.models import TransWo

# Create your models here.
class TransPM(models.Model): 
    id_trans_pm = models.AutoField(primary_key=True, db_column='id_trans_pm')  
    status = models.IntegerField(default=None,blank=True, null=True)
    bobot_total_standar = models.IntegerField(default=None,blank=True, null=True)   
    bobot_total_hasil = models.IntegerField(default=None,blank=True, null=True)   
    level_pm = models.IntegerField(default=1,blank=True, null=True)   
    kesimpulan = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    id_ref_pm = models.ForeignKey(
        RefPM, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='trans_pm_ref_pm',
        db_column='id_ref_pm'
    )
    id_trans_aset_mutasi = models.ForeignKey(
        TransAsetMutasi, on_delete=models.CASCADE, default=None, blank=True, null=True,
        db_column='id_trans_aset_mutasi'
    ) 
    id_trans_wo = models.ForeignKey(
        TransWo, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='trans_wo',
        db_column='id_trans_wo'
    )
    id_ref_hi = models.ForeignKey(
        RefHI, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='ref_hi',
        db_column='id_ref_hi'
    )
    id_ref_aset = models.ForeignKey(
        RefAset, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='ref_aset',
        db_column='id_ref_aset'
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
        db_table = 'trans_pm'

    def __str__(self):
        return self.id_trans_pm