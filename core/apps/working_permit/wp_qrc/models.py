from django.db import models  

from apps.users.models import Users

class WP_QRC(models.Model):  
    id_wp_qrc = models.AutoField(primary_key=True) 
    nama_user = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    nama_pekerjaan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    vendor = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    key_qrc = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  
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
        managed = False
        db_table = 'wp_qrc'

    def __str__(self):
        return self.id_wp_qrc 
