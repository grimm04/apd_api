 
from django.db import models  
from apps.users.models import Users

class WP_PERTANYAAN_QRC(models.Model):
    id_wp_pertanyaan_qrc = models.AutoField(primary_key=True)   
    pertanyaan = models.CharField(max_length=300, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    point = models.IntegerField(default=None, null=True)

    id_user_entri = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_entri',
        db_column='id_user_entri'
    )
    id_user_update = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_update',
        db_column='id_user_update'
    )

    tgl_entri = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    tgl_update = models.DateTimeField(auto_now=True, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'wp_pertanyaan_qrc'

    def __str__(self):
        return self.id_wp_pertanyaan_qrc  