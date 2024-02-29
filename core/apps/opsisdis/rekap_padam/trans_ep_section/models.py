from django.db import models
from apps.opsisdis.rekap_padam.trans_ep.models import TransEp 
from apps.users.models import Users
 
class TransEpSection(models.Model):
    id_trans_ep_section = models.BigAutoField(primary_key=True)
    id_trans_ep = models.ForeignKey(
        TransEp, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_trans_ep', related_name='trans_ep_section'
    )   
    section = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    beban_masuk = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    jam_masuk = models.DateTimeField(blank=True, null=True)
    id_user_entri = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_entri',
        db_column='id_user_entri'
    ) 
    tgl_entri = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    beban_sebelum = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    jam_sebelum = models.DateTimeField(blank=True, null=True)
    durasi = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ens = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True) 
    class Meta:
        managed = False
        db_table = 'trans_ep_section'
    
    # def __str__(self):
    #     return self.id_trans_ep_section
