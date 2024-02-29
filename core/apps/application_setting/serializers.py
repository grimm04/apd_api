from email.policy import default
from rest_framework import serializers
 
from .models import ApplicationSetting

class GetConfig(serializers.ModelSerializer): 
    class Meta:
        model = ApplicationSetting
        fields = ['id_app','app_name','app_name_short','logo','favicon','layout','colors','theme_mode','font','scaling','email','app_sub_name','description','company','def_generate_time',
        'def_pengukuran_teg_primer','def_pengukuran_teg_sekunder','def_nilai_cosq']

class CRApplicationSettingSerializers(serializers.ModelSerializer):
    app_name = serializers.CharField(max_length=255 , default=None, allow_blank=True, allow_null=True)
    app_name_short = serializers.CharField(max_length=50 , default=None, allow_blank=True, allow_null=True)
    logo = serializers.CharField(max_length=255 , default=None, allow_blank=True, allow_null=True) 
    favicon = serializers.CharField(max_length=255 , default=None, allow_blank=True, allow_null=True) 
    layout = serializers.CharField(max_length=255 , default=None, allow_blank=True, allow_null=True) 
    colors = serializers.CharField(max_length=255 , default=None, allow_blank=True, allow_null=True) 
    theme_mode = serializers.CharField(max_length=255 , default=None, allow_blank=True, allow_null=True) 
    font = serializers.CharField(max_length=255 , default=None, allow_blank=True, allow_null=True) 
    scaling = serializers.CharField(max_length=255 , default=None, allow_blank=True, allow_null=True) 
    email = serializers.CharField(max_length=255 , default=None, allow_blank=True, allow_null=True) 
    app_sub_name = serializers.CharField(max_length=255 , default=None, allow_blank=True, allow_null=True) 
    description = serializers.CharField(default=None, allow_blank=True, allow_null=True)
    company = serializers.CharField(max_length=255 , default=None, allow_blank=True, allow_null=True) 
    email_use_tls = serializers.BooleanField(default=True)
    email_host = serializers.CharField(max_length=255 , default=None, allow_blank=True, allow_null=True) 
    email_host_user = serializers.CharField(max_length=255 , default=None, allow_blank=True, allow_null=True) 
    email_host_password = serializers.CharField(max_length=255 , default=None, allow_blank=True, allow_null=True) 
    email_port = serializers.IntegerField(default=587) 
    max_change_life = serializers.IntegerField(default=30) 
    def_generate_time = serializers.IntegerField(default=60, allow_null=True) 
    def_pengukuran_teg_primer = serializers.DecimalField(default=150,max_digits=5, decimal_places=2,required=False) 
    def_pengukuran_teg_sekunder = serializers.DecimalField(default=20.5,max_digits=5, decimal_places=2,required=False) 
    def_nilai_cosq = serializers.DecimalField(default=0.95,max_digits=5, decimal_places=2,required=False)  

    class Meta:
        model = ApplicationSetting
        fields = '__all__'


class UDApplicationSettingSerializers(serializers.ModelSerializer):
    queryset = ApplicationSetting.objects.all()

    app_name = serializers.CharField(max_length=255 , required=False, allow_null=True)
    app_name_short = serializers.CharField(max_length=50, required=False, allow_null=True)
    logo = serializers.CharField(max_length=255 , required=False, allow_null=True) 
    favicon = serializers.CharField(max_length=255 , required=False, allow_null=True) 
    layout = serializers.CharField(max_length=255 , required=False, allow_null=True) 
    colors = serializers.CharField(max_length=255 , required=False, allow_null=True) 
    theme_mode = serializers.CharField(max_length=255 , required=False, allow_null=True) 
    font = serializers.CharField(max_length=255 , required=False, allow_null=True) 
    scaling = serializers.CharField(max_length=255 , required=False, allow_null=True) 
    email = serializers.CharField(max_length=255 , required=False, allow_null=True) 
    app_sub_name = serializers.CharField(max_length=255 , required=False, allow_null=True) 
    description = serializers.CharField(required=False, allow_null=True)
    company = serializers.CharField(max_length=255 , required=False, allow_null=True) 

    email_use_tls = serializers.BooleanField(required=False, allow_null=True)
    email_host = serializers.CharField(max_length=255 , required=False, allow_null=True) 
    email_host_user = serializers.CharField(max_length=255 , required=False, allow_null=True) 
    email_host_password = serializers.CharField(max_length=255 , required=False, allow_null=True) 
    email_port = serializers.IntegerField( required=False, allow_null=True) 

    def_generate_time = serializers.IntegerField(allow_null=True, required=True) 
    def_pengukuran_teg_primer = serializers.DecimalField(max_digits=5, decimal_places=2,required=False) 
    def_pengukuran_teg_sekunder = serializers.DecimalField(max_digits=5, decimal_places=2,required=False) 
    def_nilai_cosq = serializers.DecimalField(max_digits=5, decimal_places=2,required=False)  

    class Meta:
        model = ApplicationSetting
        fields = '__all__' 

 