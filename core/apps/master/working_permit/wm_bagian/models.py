 
from django.db import models  

class WP_BAGIAN(models.Model):
    id_wp_master_bagian = models.AutoField(primary_key=True)   
    name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    ept = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS') 
 
    class Meta:
        managed = True
        db_table = 'ref_wm_bagian'

    def __str__(self):
        return self.id_wp_master_bagian  