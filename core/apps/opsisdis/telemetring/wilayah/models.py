from django.db import models
from apps.master.jaringan.ref_lokasi.models import RefLokasi
from apps.users.models import Users

EXPORT_HEADERS = ['Datetime',  'Parent Lokasi', 'Wilayah', 'Arus (A)', 'Tegangan (kV)', 'Daya Aktif (MW)', 'Daya Reaktif (MVAR)']
EXPORT_FIELDS = ['datum', 'nama_parent_lokasi', 'nama_lokasi', 'i', 'v', 'p', 'q']
EXPORT_RELATION_FIELD = [
    {
        'ref_lokasi': [
            'nama_lokasi'
        ]
    },
    {
        'ref_parent_lokasi': [
            'nama_parent_lokasi'
        ]
    },
]

class TelemetringWilayah(models.Model):
    id_trans_tm_wilayah = models.AutoField(primary_key=True)
    datum = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    i = models.IntegerField(default=0)
    v = models.IntegerField(default=0)
    p = models.IntegerField(default=0)
    q = models.IntegerField(default=0)
    f = models.IntegerField(default=0)
    id_lokasi = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_lokasi'
    )
    tgl_entri = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    tgl_update = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    id_user_entri = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_entri',
        db_column='id_user_entri'
    )
    id_user_update = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_update',
        db_column='id_user_update'
    )

    class Meta:
        managed = True
        db_table = 'trans_tm_wilayah'

    def __str__(self):
        return self.id_trans_tm_wilayah