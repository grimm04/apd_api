from django.db import models
from apps.master.opsisdis.amr_customer.models import TelemetringAMRCustomer
import xlsxwriter

EXPORT_HEADERS = ['customer_rid', 'nama', 'frequency', 'amp_r', 'amp_s', 'amp_t', 'phase_r', 'phase_s', 'phase_t', 'volt_r', 'volt_s', 'volt_t', 'power_active', 'power_reactive', 'power_apparent', 'tgl']
EXPORT_FIELDS = ['customer_rid', 'nama', 'frequency', 'amp_r', 'amp_s', 'amp_t', 'phase_r', 'phase_s', 'phase_t', 'volt_r', 'volt_s', 'volt_t', 'power_active', 'power_reactive', 'power_apparent', 'tgl']
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
        {'name': 'FRKWENSI', 'column': 'D1:D2', 'width': 15, 'merge': True},
        {'name': 'AMR', 'column': 'E1:G1', 'width': 10, 'merge': True},
        {'name': 'R', 'column': 'E2', 'width': 5, 'merge': False},
        {'name': 'S', 'column': 'F2', 'width': 5, 'merge': False},
        {'name': 'T', 'column': 'G2', 'width': 5, 'merge': False},
        {'name': 'PHASE', 'column': 'H1:J1', 'width': 10, 'merge': True},
        {'name': 'R', 'column': 'H2', 'width': 5, 'merge': False},
        {'name': 'S', 'column': 'I2', 'width': 5, 'merge': False},
        {'name': 'T', 'column': 'J2', 'width': 5, 'merge': False},
        {'name': 'VOLT', 'column': 'K1:M1', 'width': 10, 'merge': True},
        {'name': 'R', 'column': 'K2', 'width': 5, 'merge': False},
        {'name': 'S', 'column': 'L2', 'width': 5, 'merge': False},
        {'name': 'T', 'column': 'M2', 'width': 5, 'merge': False},
        {'name': 'POWER', 'column': 'N1:P1', 'width': 10, 'merge': True},
        {'name': 'ACTIVE', 'column': 'N2', 'width': 7, 'merge': False},
        {'name': 'REACTIVE', 'column': 'O2', 'width': 7, 'merge': False},
        {'name': 'APPARENT', 'column': 'P2', 'width': 7, 'merge': False},
        {'name': 'TGL', 'column': 'Q1:Q2', 'width': 25, 'merge': True}
    ]
}]

class TelemetringAMRLoadProfile(models.Model):
    id = models.AutoField(primary_key=True)
    customer_rid = models.ForeignKey(
        TelemetringAMRCustomer, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='customer_rid'
    )
    tgl = models.DateTimeField(default=None, blank=True, null=True)
    amp_r = models.IntegerField(default=0)
    amp_s = models.IntegerField(default=0)
    amp_t = models.IntegerField(default=0)
    volt_r = models.IntegerField(default=0)
    volt_s = models.IntegerField(default=0)
    volt_t = models.IntegerField(default=0)
    power_active = models.IntegerField(default=0)
    power_reactive = models.IntegerField(default=0)
    power_apparent = models.IntegerField(default=0)
    frequency = models.IntegerField(default=0)
    phase_r = models.IntegerField(default=0)
    phase_s = models.IntegerField(default=0)
    phase_t = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'amr_trans_inst'

    def __str__(self):
        return self.id