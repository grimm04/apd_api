from django.db import models 
from apps.master.working_permit.wm_bagian.models import WP_BAGIAN 

class WP_HIRARC(models.Model):  
    id_wp_hirarc = models.AutoField(primary_key=True) 
    pekerjaan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    lokasi_pekerjaan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
 
    id_wp_master_bagian = models.ForeignKey(
        WP_BAGIAN, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_wp_master_bagian',
        db_column='id_wp_master_bagian'
    )  
    tanggal = models.DateTimeField(default=None, blank=True, null=True) 
 
    class Meta:
        managed = False
        db_table = 'wp_hirarc'

    def __str__(self):
        return self.id_wp_hirarc 
