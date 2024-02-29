from django.db import models 
from apps.users.models import Users   
from apps.master.aset.ref_aset.models import RefAset
from apps.master.aset.ref_aset_lantai.models import RefAsetLantai
from apps.master.aset.ref_aset_kondisi.models import RefAsetKondisi
from apps.master.aset.ref_aset_ruangan.models import RefAsetRuangan
from apps.master.aset.ref_aset_rak.models import RefAsetRak
from apps.master.aset.ref_aset_jenis_mutasi.models import RefAsetJenisMutasi
from apps.trans.opsisdis.trans_wo.models import TransWo

# Create your models here.
class TransAsetMutasi(models.Model): 
    id_trans_aset_mutasi = models.AutoField(primary_key=True, db_column='id_trans_aset_mutasi')  
    id_station = models.IntegerField(default=None,blank=True, null=True)
    id_bay = models.IntegerField(default=None,blank=True, null=True)
    id_pelaksana = models.IntegerField(default=None,blank=True, null=True) 

    id_ref_aset_lantai = models.ForeignKey(
        RefAsetLantai, on_delete=models.CASCADE, default=None, blank=True, null=True, 
        db_column='id_ref_aset_lantai'
    )
    id_ref_kondisi_aset = models.ForeignKey(
        RefAsetKondisi, on_delete=models.CASCADE, default=None, blank=True, null=True, 
        db_column='id_ref_kondisi_aset'
    )  
    id_trans_wo = models.ForeignKey(
        TransWo, on_delete=models.CASCADE, default=None, blank=True, null=True, 
        db_column='id_trans_wo'
    )
    id_ref_aset_ruangan = models.ForeignKey(
        RefAsetRuangan, on_delete=models.CASCADE, default=None, blank=True, null=True, 
        db_column='id_ref_aset_ruangan'
    )
    id_ref_aset_rak = models.ForeignKey(
        RefAsetRak, on_delete=models.CASCADE, default=None, blank=True, null=True, 
        db_column='id_ref_aset_rak'
    )
    id_jenis_aset_mutasi = models.ForeignKey(
        RefAsetJenisMutasi, on_delete=models.CASCADE, default=None, blank=True, null=True,
        db_column='id_jenis_aset_mutasi'
    ) 
    id_ref_aset = models.ForeignKey(
        RefAset, on_delete=models.CASCADE, default=None, blank=True, null=True, 
        db_column='id_ref_aset'
    )

    #default
    id_user_entri = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True,
        db_column='id_user_entri'
    )
    id_user_update = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_update',
        db_column='id_user_update'
    ) 
    tgl_mutasi = models.DateField(default=None, blank=True, null=True) 
    tgl_entri = models.DateField(auto_now_add=True, blank=True, null=True)
    tgl_update = models.DateField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_aset_mutasi'

    def __str__(self):
        return self.id_trans_aset_mutasi