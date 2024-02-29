# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Users(models.Model):
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(blank=True, null=True)
    id_user = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    username = models.CharField(unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    first_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    last_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    avatar = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    gender = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    phone = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    password = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at_field = models.DateTimeField(db_column='updated_at\r\n', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'users'
