from django.db import models
from apps.users.models import Users
from apps.master.aset.ref_aset.models import RefAset
from apps.master.aset.ref_aset_jenis.models import RefAsetJenis


class RefAsetExAtr(models.Model):
    class TAsetStatus(models.TextChoices):
        ACTIVE = '1'
        INACTIVE = '0' 

    status = models.IntegerField(blank=True, null=True, choices=TAsetStatus.choices, default=TAsetStatus.ACTIVE)

    id_ref_aset_ex_atr = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    satuan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
  
    id_ref_aset_jenis = models.ForeignKey(
        RefAsetJenis, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_ref_aset_jenis',
        db_column='id_ref_aset_jenis'
    )
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
        db_table = 'ref_aset_ex_atr'

    def __str__(self):
        return self.id_ref_aset_ex_atr 
