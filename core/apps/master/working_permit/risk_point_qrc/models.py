from django.db import models

class RiskPointQRC(models.Model):
    id_risk_point_qrc = models.AutoField(primary_key=True)
    low_risk_point_min = models.IntegerField(default=0)
    low_risk_point_max = models.IntegerField(default=8)
    medium_risk_point_min = models.IntegerField(default=9)
    medium_risk_point_max = models.IntegerField(default=16)
    high_risk_point = models.IntegerField(default=17)

    class Meta:
        managed = True
        db_table = 'ref_wm_risk_point_qrc'

    def __str__(self):
        return self.id_risk_point_qrc

EXPORT_HEADERS = ['id_risk_point_qrc', 'low_risk_point_min','low_risk_point_max','medium_risk_point_min','medium_risk_point_max','high_risk_point']
EXPORT_FIELDS = ['id_risk_point_qrc', 'low_risk_point_min','low_risk_point_max','medium_risk_point_min','medium_risk_point_max','high_risk_point']
EXPORT_RELATION_FIELD = [] 