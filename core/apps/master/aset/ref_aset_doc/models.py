from django.db import models
from apps.users.models import Users
from apps.master.aset.ref_aset.models import RefAset


class RefAsetDoc(models.Model):
    class TAsetStatus(models.TextChoices):
        ACTIVE = '1'
        INACTIVE = '0' 

    status = models.IntegerField(blank=True, null=True, choices=TAsetStatus.choices, default=TAsetStatus.ACTIVE)

    id_ref_aset_doc = models.AutoField(primary_key=True)
    nama_file = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    tipe = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    jenis = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    deskripsi = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
 
    id_ref_aset = models.ForeignKey(
        RefAset, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_ref_aset',
        db_column='id_ref_aset'
    )
    id_user_entri = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_entri',
        db_column='id_user_entri'
    )
    id_user_update = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_update',
        db_column='id_user_update'
    )
    tgl_entri = models.DateField(auto_now_add=True, blank=True, null=True)
    tgl_update = models.DateField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ref_aset_doc'

    def __str__(self):
        return self.id_ref_aset_doc 

EXPORT_HEADERS = ['id_ref_aset_doc', 'nama_file', 'status','tipe','jenis','deskripsi','tanggal_buat','tanggal_ubah']
EXPORT_FIELDS = ['id_ref_aset_doc', 'nama_file', 'status','tipe','jenis','deskripsi','tgl_entri','tgl_update']
EXPORT_RELATION_FIELD = [] 