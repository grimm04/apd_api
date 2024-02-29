from django.db import models
from apps.users.models import Users 
from apps.master.opsisdis.pm.ref_pm.models import RefPM 


# Create your models here.
class RefPMDetail(models.Model): 

    id_ref_pm_detail = models.AutoField(primary_key=True, db_column='id_ref_pm_detail')
    nama = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    satuan = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    id_induk_ref_pm_detail = models.IntegerField(blank=True, null=True, default=None) 
    induk = models.IntegerField(blank=True, null=True, default=None) 
    nilai_acuan = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    no_urut = models.IntegerField(blank=True, null=True, default=None) 
    tipe_data = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    nilai_pemeriksaan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 

    id_ref_pm = models.ForeignKey(
        RefPM, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_ref_pm'
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
        db_table = 'ref_pm_detail'

    def __str__(self):
        return self.id_ref_pm_detail