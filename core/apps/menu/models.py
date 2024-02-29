from django.db import models


# Create your models here.
class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    idParent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    display = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    path = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    icon = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    privileges = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', null=True)
    hidden = models.BooleanField(default=False)
    search = models.BooleanField(default=False)
    divider = models.BooleanField(default=False)
    no = models.IntegerField(default=0)
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.id
