from django.db import models
from apps.master.pegawai.jabatan.models import Jabatan
from apps.master.pegawai.departemen.models import Departemen
from apps.users.models import Users

class ApprovalManagementWP(models.Model):
    id_approval_management_wp = models.AutoField(primary_key=True)
    id_jabatan = models.ForeignKey(
        Jabatan, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_jabatan'
    )
    id_user = models.ForeignKey(
        Users, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_user'
    )
    id_departemen = models.ForeignKey(
        Departemen, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_departemen'
    )
    nama_pegawai = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    nama_jabatan = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    nama_bagian = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = True
        db_table = 'ref_wm_approval_management_wp'

    def __str__(self):
        return self.id_approval_management_wp
 
EXPORT_HEADERS = ['id_approval_management_wp', 'nama_pegawai', 'nama_jabatan']
EXPORT_FIELDS = ['id_approval_management_wp', 'nama_pegawai', 'nama_jabatan']
EXPORT_RELATION_FIELD = [] 