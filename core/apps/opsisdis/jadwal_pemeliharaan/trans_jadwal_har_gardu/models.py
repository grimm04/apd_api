from django.db import models
from apps.opsisdis.jadwal_pemeliharaan.trans_jadwal_har.models import TransJadwalHar
from apps.master.jaringan.ref_lokasi.models import RefLokasi 

class TransJadwalHarGardu(models.Model):
    id_trans_jadwal_har_gardu = models.AutoField(primary_key=True) 
    id_gardu = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_gardu'
    )
    id_trans_jadwal_har = models.ForeignKey(
        TransJadwalHar, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_trans_jadwal_har', related_name="har_gardu"
    ) 

    class Meta:
        managed = False
        db_table = 'trans_jadwal_har_gardu'
