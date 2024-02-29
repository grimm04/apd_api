from django.db import models

class LaranganTanggungJawabMitra(models.Model):
    id_larangan_tanggung_jawab_mitra = models.AutoField(primary_key=True)
    uraian = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = True
        db_table = 'ref_wm_larangan_tanggung_jawab_mitra'

    def __str__(self):
        return self.id_larangan_tanggung_jawab_mitra

 
EXPORT_HEADERS = ['id_larangan_tanggung_jawab_mitra', 'uraian']
EXPORT_FIELDS = ['id_larangan_tanggung_jawab_mitra', 'uraian']
EXPORT_RELATION_FIELD = [] 