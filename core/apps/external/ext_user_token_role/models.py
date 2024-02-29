from django.db import models
from apps.external.ext_user_token.models import ExtUserToken
from apps.external.ext_module.models import ExtModule


# Create your models here.
class ExtUserTokenRole(models.Model):
    id_token_role = models.AutoField(primary_key=True)
    id_token = models.ForeignKey(
        ExtUserToken, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_token',
        db_column='id_token'
    )
    id_module = models.ForeignKey(
        ExtModule, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_module',
        db_column='id_module'
    )

    class Meta:
        managed = False
        db_table = 'ext_user_token_role'

    def __str__(self):
        return self.id_token_role
