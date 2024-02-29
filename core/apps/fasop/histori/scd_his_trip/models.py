from django.db import models  

class SCD_HIS_TRIP(models.Model):
    id_his_trip = models.AutoField(primary_key=True)  
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
    
    trip = models.IntegerField(default=None,blank=True, null=True)
    ocr = models.IntegerField(default=None,blank=True, null=True)
    gfr = models.IntegerField(default=None,blank=True, null=True)

    i = models.FloatField(default=None, blank=True, null=True)
    ifr = models.FloatField(default=None, blank=True, null=True)
    ifs = models.FloatField(default=None, blank=True, null=True)
    ift = models.FloatField(default=None, blank=True, null=True)
    ifn = models.FloatField(default=None, blank=True, null=True)
    cek_trip = models.FloatField(default=None, blank=True, null=True)

    jenis = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    cb_open = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    wilayah_padam = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
     
    datum_cb_open = models.DateTimeField(default=None, blank=True, null=True) 
    datum_created = models.DateTimeField(default=None, blank=True, null=True) 
    cbtr = models.IntegerField(default=None,blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'scd_his_trip'

    def __str__(self):
        return self.id 

EXPORT_HEADERS = ['id', 'B1','b2','b3','element', 'Datetime Trip', 'Datetime Normal','OCR','GFR','I Beban','IGR','igs','igt','ign']
#blm bisa nesed jenis rtu
EXPORT_FIELDS = ['id', 'b1', 'b2','b3','elem','datum_1','datum_2','ocr','grf','i','ifr','ifs','ift','ifn']
EXPORT_RELATION_FIELD = [] 