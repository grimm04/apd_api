from django.db import models 
from apps.users.models import Users

class USER_HIS_PASSWORD(models.Model):
    id_user_his_password = models.AutoField(primary_key=True)
    password = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    id_user = models.ForeignKey(
        Users, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_user'
    )

    class Meta:
        managed = True
        db_table = 'users_his_password'

    def __str__(self):
        return self.id_user_his_password
 