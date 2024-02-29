from django.db import models

# Create your models here.
from django.db import models

from apps.master.fasop.point_type.models import PointType


class CPoint(models.Model):
    point_number = models.AutoField(primary_key=True)
    id_pointtype = models.ForeignKey(
        PointType, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_pointtype', related_name='c_point'
    )
    point_name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    point_text = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    description = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    point_type = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    active = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    aor_id = models.IntegerField()
    aor_id_dw = models.IntegerField()
    measurement_type = models.IntegerField()
    tariff_group_id = models.IntegerField()
    ctrl_area_int_id = models.IntegerField()
    ctrl_area_ext_id = models.IntegerField()
    meas_unit = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    state_set_id = models.IntegerField()
    collection_rate = models.IntegerField()
    absolute_error = models.IntegerField()
    significant_digits = models.IntegerField()
    energy_type = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    import_export = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    counter_type = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    scaling_facktor = models.IntegerField()
    rollover_limit = models.IntegerField()
    precision_processing = models.IntegerField()
    precision = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    ddc_trigger_report_flag = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    system_id = models.IntegerField()
    collection_delay = models.IntegerField()
    value = models.IntegerField()
    status_network = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    update_network = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    kinerja = models.IntegerField()
    point_class = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    send_telegram = models.IntegerField()
    capture_telemetring = models.IntegerField()
    format_pesan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    durasi_perubahan = models.IntegerField()
    rc = models.IntegerField()
    trip = models.IntegerField()
    rc_telegram = models.IntegerField()
    trip_telegram = models.IntegerField()
    status = models.IntegerField()
    wilayah = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    path1 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    path2 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    path3 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    path4 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    path5 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    path1text = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    path2text = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    path3text = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    path4text = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    path5text = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    last_update = models.DateTimeField(auto_now=True, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scd_c_point'

    def __str__(self):
        return self.point_number
    
    @property
    def pointtype_name(self):
        return self.id_pointtype.name


EXPORT_HEADERS = ['jenis_point','station', 'point_number','point_name','point_text','tipe_point','send_telegram','telemark_30M','b1','b2','b3','element','info','value']
EXPORT_FIELDS = ['jenispoint', 'path1text','point_number', 'point_name','point_text','jenispoint','send_telegram','capture_telemetring','path3text','path4text','path5text','description','description','value']
EXPORT_RELATION_FIELD = [
            {'pointtype':['pointtype_name','jenispoint']},  
] 