from django.db import models
from apps.users.models import Users 
 
from apps.master.opsisdis.wo.ref_wo_status.models import RefWOStatus
from apps.trans.opsisdis.trans_wo.models import TransWo

# Create your models here.
class TransWoLogStatus(models.Model): 
    id_wo_log_status = models.AutoField(primary_key=True, db_column='id_wo_log_status')
 
    id_ref_wo_status = models.ForeignKey(
        RefWOStatus, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_wo_status',
        db_column='id_ref_wo_status'
    )
    id_wo = models.ForeignKey(
        TransWo, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_wo',
        db_column='id_wo'
    )
    
    #default
    id_user_entri = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_entri',
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
        db_table = 'trans_wo_log_status'

    def __str__(self):
        return self.id_wo_log_status