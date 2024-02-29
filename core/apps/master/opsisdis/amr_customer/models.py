from django.db import models
from apps.master.jaringan.ref_lokasi.models import RefLokasi

EXPORT_HEADERS = ['customer_rid', 'meter_id', 'meter_type', 'rate', 'modem_adr', 'nama', 'alamat', 'lok', 'daya', 'bapm', 'faktor_kali', 'nofa', 'goltarif', 'kodegardu', 'ref_lokasi']
EXPORT_FIELDS = ['customer_rid', 'meter_id', 'meter_type', 'rate', 'modem_adr', 'nama', 'alamat', 'lok', 'daya', 'bapm', 'faktor_kali', 'nofa', 'goltarif', 'kodegardu', 'nama_lokasi']
EXPORT_RELATION_FIELD = [
    {
        'ref_lokasi': [
            'nama_lokasi'
        ]
    }
]

class TelemetringAMRCustomer(models.Model):
    id = models.AutoField(primary_key=True)
    customer_rid = models.IntegerField(default=0)
    meter_id = models.CharField(max_length=24, db_collation='SQL_Latin1_General_CP1_CI_AS')
    meter_type = models.IntegerField(default=0)
    rate = models.CharField(max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS')
    modem_adr = models.IntegerField(default=0)
    nama = models.CharField(max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    alamat = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    lok = models.CharField(max_length=70, db_collation='SQL_Latin1_General_CP1_CI_AS')
    daya = models.IntegerField(default=0)
    bapm = models.CharField(max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS')
    faktor_kali = models.IntegerField(default=0)
    nofa = models.CharField(max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS')
    goltarif = models.CharField(max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS')
    kodegardu = models.CharField(max_length=32, db_collation='SQL_Latin1_General_CP1_CI_AS')
    id_lokasi = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_lokasi',
        related_name='%(class)s_id_lokasi'
    )

    class Meta:
        managed = True
        db_table = 'amr_customer'

    def __str__(self):
        return self.id