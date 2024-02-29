 
from django.db import models  
from apps.working_permit.wp_online.models import WP_ONLINE 

class WP_ONLINE_PEKERJA(models.Model):
    id_wp_online_pekerja = models.AutoField(primary_key=True)   
    nama_pekerja = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')  

    id_wp_online = models.ForeignKey(
        WP_ONLINE, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_wp_online',
        db_column='id_wp_online'
    ) 
    class Meta:
        managed = True
        db_table = 'wp_online_pekerja'

    def __str__(self):
        return self.id_wp_online_pekerja  