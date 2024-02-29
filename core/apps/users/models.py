from operator import mod
from statistics import mode
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from apps.master.pegawai.departemen.models import Departemen
from apps.master.pegawai.ref_regu_petugas.models import REF_REGU_PETUGAS_MODELS
from apps.master.pegawai.jabatan.models import Jabatan
from apps.master.pegawai.perusahaan.models import Perusahaan
from apps.roles.models import Roles

class CustomAccountManager(BaseUserManager):

    def create_user(self, email, username, fullname, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))
        if not username:
            raise ValueError(_('You must provide an username'))

        user = self.model(email=self.normalize_email(email),
                          username=username,
                          fullname=fullname,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, fullname, password):

        user = self.model(email=self.normalize_email(email),
                          username=username,
                          fullname=fullname,
                          password=password
                          )

        user.is_staff = True
        user.is_superuser = True
        user.is_active = True

        user.set_password(password)
        user.save()
        return user


class Users(AbstractBaseUser, PermissionsMixin): 

    class TUserStatus(models.TextChoices):
        ACTIVE = 'active'
        INACTIVE = 'inactive'
        BLOCK = 'block'

    class TUserGender(models.TextChoices):
        L = 'L'
        P = 'P'

    id_user = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # roleId = models.IntegerField(default=None, blank=True)
    roleId = models.ForeignKey(
        Roles, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_roleId',
        db_column='roleId'
    )
    nip = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=10, choices=TUserStatus.choices, default=TUserStatus.ACTIVE)
    fullname = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=255, blank=True,unique=True)
    sap = models.CharField(max_length=100, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=1, choices=TUserGender.choices) 
    avatar = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    signature = models.CharField(max_length=255, blank=True) 
    last_change_pwd = models.DateTimeField(default=None, blank=True, null=True)
 
    id_perusahaan = models.ForeignKey(
        Perusahaan, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_perusahaan',
        db_column='id_perusahaan'
    )
    id_jabatan = models.ForeignKey(
        Jabatan, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_jabatan',
        db_column='id_jabatan'
    )
    id_departemen = models.ForeignKey(
        Departemen, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_departemen',
        db_column='id_departemen'
    )
    id_ref_regu_petugas = models.ForeignKey(
        REF_REGU_PETUGAS_MODELS, on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_ref_regu_petugas'
    )
    akses_login = models.BooleanField(default=False)


    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['fullname', 'password']

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username
