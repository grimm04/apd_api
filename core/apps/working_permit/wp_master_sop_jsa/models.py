from django.db import models 
from apps.master.working_permit.wm_bagian.models import WP_BAGIAN


class WP_MASTER_SOP_JSA(models.Model):  
    id_wp_master_sop_jsa = models.AutoField(primary_key=True) 
    judul_pekerjaan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    nomor = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    nama_file = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    langkah1 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    langkah2 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    langkah3 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    langkah4 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    langkah5 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    langkah6 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    langkah7 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    langkah8 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    langkah9 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    langkah10 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    langkah11 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    langkah12 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    langkah13 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    langkah14 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    langkah15 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    potensi1 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    potensi2 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    potensi3 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    potensi4 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    potensi5 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    potensi6 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    potensi7 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    potensi8 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    potensi9 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    potensi10 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    potensi11 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    potensi12 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    potensi13 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    potensi14 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    potensi15 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    pengendalian1 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')   
    pengendalian2 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')   
    pengendalian3 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')   
    pengendalian4 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')   
    pengendalian5 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')   
    pengendalian6 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')   
    pengendalian7 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')   
    pengendalian8 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')   
    pengendalian9 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')   
    pengendalian10 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')   
    pengendalian11 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')   
    pengendalian12 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')   
    pengendalian13 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')   
    pengendalian14 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')   
    pengendalian15 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')   
 
    id_wp_master_bagian = models.ForeignKey(
        WP_BAGIAN, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_ref_aset',
        db_column='id_wp_master_bagian'
    )  
    tgl_entri = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    tgl_update = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_master_sop_jsa'

    def __str__(self):
        return self.id_wp_master_sop_jsa 
