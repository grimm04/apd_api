from django.db import models 

# Create your models here.
class ApplicationSetting(models.Model): 
    id_app = models.AutoField(primary_key=True)
    app_name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS' ,  default=None, blank=True, null=True)
    app_name_short = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS' , default=None, blank=True, null=True)
    logo = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS' , default=None, blank=True, null=True) 
    favicon = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS' , default=None, blank=True, null=True) 
    layout = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS' , default=None, blank=True, null=True) 
    colors = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS' , default=None, blank=True, null=True) 
    theme_mode = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS' , default=None, blank=True, null=True) 
    font = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS' , default=None, blank=True, null=True) 
    scaling = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS' , default=None, blank=True, null=True) 
    email = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS' , default=None, blank=True, null=True) 
    app_sub_name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS' , default=None, blank=True, null=True) 
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS' , default=None, blank=True, null=True) 
    company = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS' , default=None, blank=True, null=True) 
    email_use_tls = models.BooleanField(default=True)
    email_host = models.CharField(max_length=1024, default=None, blank=True, null=True)
    email_host_user = models.CharField(max_length=255, default=None, blank=True, null=True)
    email_host_password = models.CharField(max_length=255, default=None, blank=True, null=True)
    email_port = models.PositiveSmallIntegerField(default=587, blank=True, null=True)
    max_change_life = models.IntegerField(default=30, blank=True, null=True)
    def_generate_time = models.IntegerField(default=60, blank=True, null=True) 
    def_pengukuran_teg_primer = models.DecimalField(default=None,max_digits=5, decimal_places=2,blank=True, null=True)
    def_pengukuran_teg_sekunder = models.DecimalField(default=None,max_digits=5, decimal_places=2,blank=True, null=True)
    def_nilai_cosq = models.DecimalField(default=None,max_digits=5, decimal_places=2,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'application_setting'

    def __str__(self):
        return self.id_app