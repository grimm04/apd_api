from django.db import models 
from apps.users.models import Users
from apps.master.jaringan.ref_lokasi.models import RefLokasi


class REF_PEGAWAI(models.Model):  
    id_pegawai = models.AutoField(primary_key=True)  
 
    id_user = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user',
        db_column='id_user'
    )  
    id_ref_lokasi = models.ForeignKey(
        RefLokasi, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user',
        db_column='id_ref_lokasi'
    )   
 
    tgl_entri = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    tgl_update = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ref_pegawai'

    def __str__(self):
        return self.id_pegawai 
