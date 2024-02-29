from django.db import models
from apps.users.models import Users
from apps.master.aset.ref_aset.models import RefAset
from apps.master.aset.ref_aset_ex_atr.models import RefAsetExAtr


class RefAsetExtAtr(models.Model):
    class TAsetStatus(models.TextChoices):
        ACTIVE = '1'
        INACTIVE = '0' 

    status = models.IntegerField(blank=True, null=True, choices=TAsetStatus.choices, default=TAsetStatus.ACTIVE)

    id_ref_aset_ext_atr = models.AutoField(primary_key=True)
    nilai = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
 
    id_ref_aset = models.ForeignKey(
        RefAset, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_ref_aset',
        db_column='id_ref_aset'
    ) 
    id_ref_aset_ex_atr = models.ForeignKey(
        RefAsetExAtr, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_ref_aset_ex_atr',
        db_column='id_ref_aset_ex_atr'
    ) 
    tgl_entri = models.DateField(auto_now_add=True, blank=True, null=True)
    tgl_update = models.DateField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ref_aset_ext_atr'

    def __str__(self):
        return self.id_ref_aset_ext_atr 
