from django.db import models
import datetime
from apps.users.models import Users 
from apps.master.opsisdis.wo.ref_wo_jenis.models import RefWOJenis 

# Create your models here.
class TransWo(models.Model): 
    id_trans_wo = models.AutoField(primary_key=True, db_column='id_trans_wo')
    nomor = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    uraian = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_pelaksana = models.IntegerField(blank=True, null=True)
    id_station = models.IntegerField(blank=True, null=True)   

    id_ref_wo_jenis = models.ForeignKey(
        RefWOJenis, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_jenis_wo',
        db_column='id_ref_wo_jenis'
    )
    # id_wo_log_status = models.ForeignKey(
    #     TransWoLogStatus, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_wo_log_status',
    #     db_column='id_wo_log_status'
    # )
    
    #default
    id_user_entri = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_entri',
        db_column='id_user_entri'
    )
    id_user_update = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_update',
        db_column='id_user_update'
    )
    tgl_mulai = models.DateField(default=None, blank=True, null=True)
    tgl_selesai = models.DateField(default=None, blank=True, null=True)
    tgl_entri = models.DateField(auto_now_add=True, blank=True, null=True)
    tgl_update = models.DateField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_wo'

    def __str__(self):
        return self.id_trans_wo