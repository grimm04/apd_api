from django.db import models  

class SCD_HIS_RC(models.Model):
    id_his_rc = models.AutoField(primary_key=True)  
    path1 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    path2 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    path3 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    path4 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    path5 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    b1 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    b2 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    b3 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    elem = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    info = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 

    datum_1 = models.DateTimeField(default=None, blank=True, null=True)
    status_1 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    datum_2 = models.DateTimeField(default=None, blank=True, null=True)
    status_2 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    msgoperator = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    cek_remote = models.IntegerField(default=None,blank=True, null=True)

    berhasil = models.IntegerField(default=None,blank=True, null=True)
    gagal = models.IntegerField(default=None,blank=True, null=True)
    kinerja = models.FloatField(default=None,blank=True, null=True)

    datum_created = models.DateTimeField(default=None, blank=True, null=True) 
    class Meta:
        managed = True
        db_table = 'scd_his_rc'

    def __str__(self):
        return self.id_his_rc 

EXPORT_HEADERS = ['id','Kinerja','rtu', 'B1','b3','element', 'Operator', 'Tanggal Eksekusi','Status Eksekusi','Tanggal Response','Status Response','DUrasi (detik)','Kesimpulan'] 
EXPORT_FIELDS = ['id', 'kinerja', 'path1','b1','b3','elem','msgoperator','datum_1','status_1','datum_2','status_2','','']
EXPORT_RELATION_FIELD = [] 