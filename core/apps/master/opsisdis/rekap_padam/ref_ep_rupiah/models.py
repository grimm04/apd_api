from django.db import models 


# Create your models here.
class RefEpRupiah(models.Model):
    id_ref_ep_rupiah = models.AutoField(primary_key=True) 
    nilai = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ref_ep_rupiah' 

    def __str__(self):
        return self.id_ref_ep_rupiah

EXPORT_HEADERS = ['id_ref_ep_rupiah', 'nilai']
EXPORT_FIELDS = ['id_ref_ep_rupiah', 'nilai']
EXPORT_RELATION_FIELD = [] 