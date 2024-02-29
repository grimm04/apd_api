from django.db import models

class Frekuensi(models.Model):
    id_meter = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status = models.BigIntegerField(default=0)
    lokasi = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    general_slaveid = models.IntegerField(default=0)
    general_address = models.IntegerField(default=0)
    general_scale = models.IntegerField(default=0)
    general_mode = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    general_koneksi = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    general_logging = models.IntegerField(default=0)
    general_interval_logging = models.IntegerField(default=0)
    serial_port = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    serial_baudrate = models.IntegerField(default=0)
    serial_bytesize = models.IntegerField(default=0)
    serial_parity = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    serial_stopbits = models.IntegerField(default=0)
    serial_xonxoff = models.IntegerField(default=0)
    ip_host = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    ip_port = models.IntegerField(default=0)
    # datum_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scd_ref_frek'

    def __str__(self):
        return self.id_meter

EXPORT_HEADERS = ['id_meter', 'nama','status','lokasi']
EXPORT_FIELDS = ['id_meter','nama','status','lokasi']
EXPORT_RELATION_FIELD =  []