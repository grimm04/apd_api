 
from django.db import models  
from apps.master.working_permit.wm_bagian.models import WP_BAGIAN

from apps.users.models import Users
class WP_APROVAL_TTD(models.Model):
    id_wp_aproval_ttd = models.AutoField(primary_key=True)    
    id_user = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user',
        db_column='id_user'
    ) 
    id_wp_master_bagian = models.ForeignKey(
        WP_BAGIAN, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_bagian',
        db_column='id_wp_master_bagian'
    ) 
    class Meta:
        managed = True
        db_table = 'wp_aproval_ttd'

    def __str__(self):
        return self.id_wp_aproval_ttd  