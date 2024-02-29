from django.db import models

# Create your models here.
from django.db import models

from apps.master.fasop.point_type.models import PointType


# Create your models here.
class PointTypeState(models.Model):
    id_pointtype_state = models.AutoField(primary_key=True)
    id_pointtype = models.ForeignKey(
        PointType, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_pointtype'
    )
    name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status = models.IntegerField(blank=True, null=True, default=None)
    valid = models.IntegerField(blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    statekey = models.IntegerField(blank=True, null=True, default=None)
    quality_code = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                    blank=True, null=True, default=None)

    class Meta:
        managed = False
        db_table = 'scd_pointtype_state'

    def __str__(self):
        return self.id_pointtype_state


EXPORT_HEADERS = ['id_pointtype_state', 'jenis point','name', 'status','valid','statekey','status','quality_code']
EXPORT_FIELDS = ['id_pointtype_state','pointtype_name', 'name', 'status','valid', 'statekey','status','quality_code']
EXPORT_RELATION_FIELD = [
            {'pointtype':['pointtype_name']},  
        ] 