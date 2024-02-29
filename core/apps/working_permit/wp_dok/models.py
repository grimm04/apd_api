from django.db import models  
from apps.working_permit.wp_online.models import WP_ONLINE


class WP_DOK(models.Model):  
    id_wp_dok = models.AutoField(primary_key=True)  
    nama_dok = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS') 
 
    id_wp_online = models.ForeignKey(
        WP_ONLINE, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_qrc',
        db_column='id_wp_online'
    )    

    tgl_entri = models.DateTimeField(auto_now_add=True, blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'wp_dok'

    def __str__(self):
        return self.id_wp_dok 
