 
from django.db import models  
from apps.users.models import Users

class WP_TTD_ONLINE(models.Model):
    id_wp_ttd_online = models.AutoField(primary_key=True)   
    nama = models.CharField(max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS')   
    nama_file = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')   
    group_file = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')   

    id_user = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user',
        db_column='id_user'
    )

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
        db_table = 'wp_ttd_online'

    def __str__(self):
        return self.id_wp_ttd_online  