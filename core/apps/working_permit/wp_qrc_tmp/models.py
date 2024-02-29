from django.db import models 
from apps.working_permit.wp_qrc.models import WP_QRC
from apps.master.working_permit.pertanyaan_qrc.models import PertanyaanQRC



class WP_QRC_TMP(models.Model):  
    id_wp_qrc_tmp = models.AutoField(primary_key=True)  
    ada = models.IntegerField(default=None, null=True)
  
    id_pertanyaan_qrc = models.ForeignKey(
        PertanyaanQRC, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_pertanyaan_qrc',
        db_column='id_pertanyaan_qrc'
    )   

    class Meta:
        managed = False
        db_table = 'wp_qrc_tmp'

    def __str__(self):
        return self.id_wp_qrc_tmp 
