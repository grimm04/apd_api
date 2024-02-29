from django.db import models

class PertanyaanQRC(models.Model):
    id_pertanyaan_qrc = models.AutoField(primary_key=True)
    pertanyaan_qrc = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    pertanyaan_qrc_point = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'ref_wm_pertanyaan_qrc'

    def __str__(self):
        return self.id_pertanyaan_qrc

EXPORT_HEADERS = ['id_pertanyaan_qrc', 'pertanyaan_qrc','pertanyaan_qrc_point']
EXPORT_FIELDS = ['id_pertanyaan_qrc', 'pertanyaan_qrc','pertanyaan_qrc_point']
EXPORT_RELATION_FIELD = [] 