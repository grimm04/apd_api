from django.db import models
from apps.users.models import Users


# Create your models here.
class ExtUserToken(models.Model):
    id_token = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    token = models.CharField(max_length=999999999999, db_collation='SQL_Latin1_General_CP1_CI_AS')
    id_user = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user',
        db_column='id_user'
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ext_user_token'

    def __str__(self):
        return self.id_token
