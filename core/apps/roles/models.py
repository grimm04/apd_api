from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Roles(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    level = models.IntegerField(default=0)
    privileges = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles_roles'

    def __str__(self):
        return self.id
