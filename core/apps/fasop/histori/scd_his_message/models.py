 
from django.db import models  

class SCD_HIS_MESSAGE(models.Model):
    id = models.AutoField(primary_key=True) 

    msec = models.IntegerField(default=None, blank=True, null=True)
    chron_order = models.IntegerField(default=None, blank=True, null=True)
    aor_id = models.IntegerField(default=None, blank=True, null=True)
    site = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    path1 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    path2 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    path3 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    path4 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    path5 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    priority = models.IntegerField(default=None, blank=True, null=True)
    console = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    indicator = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    limit = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    message_text = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    msgclass = models.IntegerField(default=None, blank=True, null=True)
    operator = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    unit = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    value = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    color = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    comment_text = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    event_type = models.IntegerField(default=None, blank=True, null=True)
    comment_id = models.IntegerField(default=None, blank=True, null=True)
    cc_id = models.IntegerField(default=None, blank=True, null=True)
    tx_mode = models.IntegerField(default=None, blank=True, null=True)
    system_msec = models.IntegerField(default=None, blank=True, null=True)
    ack = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    b1 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    b2 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    b3 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    elem = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    info = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    vartext = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    msgstatus = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    tag = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    msgoperator = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    msgclasstext = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    info_type = models.IntegerField(default=None, blank=True, null=True)
    source = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status_rtu = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    cek_trip = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 

    # point_number = models.ForeignKey(
    #     FASOPMASTER, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='point_number'
    # ) 

    #date
    time_stamp = models.DateTimeField(default=None, blank=True, null=True) 
    system_time_stamp = models.DateTimeField(auto_now_add=True, blank=True, null=True) 
 
    class Meta:
        managed = True
        db_table = 'scd_his_message'

    def __str__(self):
        return self.id 

EXPORT_HEADERS = ['id', 'Tanggal','b1text','b2text', 'b3text', 'elementtext','info','value','msgstatus','msgoperator']
EXPORT_FIELDS = ['id', 'time_stamp','b1','b2','b3','elem','info','vartext','msgstatus','msgoperator']
EXPORT_RELATION_FIELD = [] 