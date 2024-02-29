from django.db import models 
from apps.master.jaringan.ref_lokasi.models import RefLokasi


class DAF_SLD_GI(models.Model):  
    id_daf_sld_gi = models.AutoField(primary_key=True) 
    nama_file = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    kelompok = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    keterangan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
 
    id_gardu_induk = models.ForeignKey(
        RefLokasi, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_gardu_induk',
        db_column='id_gardu_induk'
    )  
    tgl_upload = models.DateTimeField(auto_now_add=True, blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'daf_sld_gi'

    def __str__(self):
        return self.id_daf_sld_gi 
