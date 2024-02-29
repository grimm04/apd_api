from django.db import models

# Create your models here.
from django.db import models

from apps.master.fasop.telegram_group.models import TelegramGroup


# Create your models here.
class PointType(models.Model):
    id_pointtype = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status = models.IntegerField(blank=True, null=True, default=None)
    id_induk_pointtype = models.IntegerField(blank=True, null=True, default=None)
    datum_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    log_his = models.IntegerField(blank=True, null=True, default=None)
    jenispoint = models.CharField(max_length=999999999999, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                  blank=True, null=True, default=None)
    show_grafik = models.IntegerField(blank=True, null=True, default=None)
    no_urut = models.IntegerField(blank=True, null=True, default=None)
    warna = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                             null=True, default=None)
    send_telegram = models.IntegerField(blank=True, null=True, default=None)
    format_pesan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                    null=True, default=None)
    durasi_perubahan = models.IntegerField(blank=True, null=True, default=None)
    id_telegram_group = models.ForeignKey(
        TelegramGroup, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_telegram_group'
    ) 
    id_induk_pointtype = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_induk_pointtype',
        related_name='child_pointtype'
    )
    nama_table_rtl = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, default=None)
    nama_table_his = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, default=None)
    nama_table_rtl = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, default=None)
    nama_table_kin_hari = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, default=None)
    nama_table_kin_bulan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, default=None)
    nama_table_ref = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, default=None)

    class Meta:
        managed = False
        db_table = 'scd_pointtype'

    def __str__(self):
        return self.id_pointtype

EXPORT_HEADERS = ['nama', 'jenis point','no_urut', 'group telegram','tampil dashboard','kirim telegram','status','format_pesan']
EXPORT_FIELDS = ['name','jenispoint', 'no_urut', 'nama_group','show_grafik', 'send_telegram','status','format_pesan']
EXPORT_RELATION_FIELD = [
            {'telegram_group':['nama_group']},  
        ] 