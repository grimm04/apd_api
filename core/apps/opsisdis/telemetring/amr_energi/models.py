from django.db import models
from apps.master.opsisdis.amr_customer.models import TelemetringAMRCustomer

EXPORT_HEADERS = ['customer_rid', 'nama', 'fk', 'kwh_prev', 'kvarh_prev', 'rate1_prev', 'rate2_prev', 'rate3_prev', 'kwh', 'kvarh', 'rate1', 'rate2', 'rate3', 'maxdem', 'tgl']
EXPORT_FIELDS = ['customer_rid', 'nama', 'fk', 'kwh_prev', 'kvarh_prev', 'rate1_prev', 'rate2_prev', 'rate3_prev', 'kwh', 'kvarh', 'rate1', 'rate2', 'rate3', 'maxdem', 'tgl']
EXPORT_RELATION_FIELD = [
    {
        'ref_customer': [
            'nama'
        ]
    }
]
EXPORT_HEADERS_CUSTOM_XLSX = [{
    'row_start': 2,
    'data': [
        {'name': 'CUSTOMER RID', 'column': 'B1:B2', 'width': 15, 'merge': True},
        {'name': 'CUSTOMER NAME', 'column': 'C1:C2', 'width': 15, 'merge': True},
        {'name': 'FAKTOR KALI', 'column': 'D1:D2', 'width': 15, 'merge': True},
        {'name': 'STAND AWAL', 'column': 'E1:I1', 'width': 10, 'merge': True},
        {'name': 'KWH', 'column': 'E2', 'width': 5, 'merge': False},
        {'name': 'KVRAH', 'column': 'F2', 'width': 5, 'merge': False},
        {'name': 'RATE 1', 'column': 'G2', 'width': 5, 'merge': False},
        {'name': 'RATE 2', 'column': 'H2', 'width': 5, 'merge': False},
        {'name': 'RATE 3', 'column': 'I2', 'width': 5, 'merge': False},
        {'name': 'STAND AKHIR', 'column': 'J1:N1', 'width': 10, 'merge': True},
        {'name': 'KWH', 'column': 'J2', 'width': 5, 'merge': False},
        {'name': 'KVRAH', 'column': 'K2', 'width': 5, 'merge': False},
        {'name': 'RATE 1', 'column': 'L2', 'width': 5, 'merge': False},
        {'name': 'RATE 2', 'column': 'M2', 'width': 5, 'merge': False},
        {'name': 'RATE 3', 'column': 'N2', 'width': 5, 'merge': False},
        {'name': 'MAXDEM', 'column': 'O1:O2', 'width': 10, 'merge': True},
        {'name': 'TGL', 'column': 'P1:P2', 'width': 25, 'merge': True}
    ]
}]


class TelemetringAMREnergi(models.Model):
    id = models.AutoField(primary_key=True)
    customer_rid = models.ForeignKey(
        TelemetringAMRCustomer, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='customer_rid'
    )
    tgl = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    kwh = models.IntegerField(default=0)
    kvarh = models.IntegerField(default=0)
    kvah = models.IntegerField(default=0)
    tgl_maxdem = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    maxdem = models.IntegerField(default=0)
    rate1 = models.IntegerField(default=0)
    rate2 = models.IntegerField(default=0)
    rate3 = models.IntegerField(default=0)
    rate1_prev = models.IntegerField(default=0)
    rate2_prev = models.IntegerField(default=0)
    rate3_prev = models.IntegerField(default=0)
    kwh_prev = models.IntegerField(default=0)
    fk = models.IntegerField(default=0)
    kvarh_prev = models.IntegerField(default=0)
    tgl_capture = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    tgl_prev = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    kvah_prev = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'amr_trans_export'

    def __str__(self):
        return self.id