from django.db import models 
from apps.working_permit.wp_hirarc.models import WP_HIRARC


class WP_HIRARC_DETAIL(models.Model):  
    id_wp_hirarc_detail = models.AutoField(primary_key=True) 
    kegiatan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    bahaya = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    resiko_bahaya = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    peluang = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    akibat = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    tingkat_resiko = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    pengendalian = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    penanggung_jawab = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    peluang2 = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    akibat2 = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    tingkat_resiko2 = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status_pengendalian = models.BooleanField(default=True)

 
    id_wp_hirarc = models.ForeignKey(
        WP_HIRARC, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='hirarc_detail',
        db_column='id_wp_hirarc'
    )   

    class Meta:
        managed = False
        db_table = 'wp_hirarc_detail'

    def __str__(self):
        return self.id_wp_hirarc_detail 
