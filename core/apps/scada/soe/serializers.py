from rest_framework import serializers
from .models import ScadaSOEModels
 

class ScadaSOESerializer(serializers.ModelSerializer): 

    msec = serializers.IntegerField(default=None)
    chron_order = serializers.IntegerField(default=None)
    aor_id = serializers.IntegerField(default=None)
    site = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    path1 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    path2 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    path3 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    path4 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    path5 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    priority = serializers.IntegerField(default=None)
    console = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    indicator = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    limit = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    message_text = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    msgclass = serializers.IntegerField(default=None)
    operator = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    unit = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    value = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    color = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    comment_text = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    event_type = serializers.IntegerField(default=None)
    comment_id = serializers.IntegerField(default=None)
    cc_id = serializers.IntegerField(default=None)
    tx_mode = serializers.IntegerField(default=None)
    system_msec = serializers.IntegerField(default=None)
    ack = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    b1 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    b2 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    b3 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    elem = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    info = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    vartext = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    msgstatus = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    tag = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    msgoperator = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    msgclasstext = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    info_type = serializers.IntegerField(default=None)
    source = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    status_rtu = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None) 
    cek_trip = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None) 

    time_stamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S") 
    system_time_stamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")  

    class Meta:
        model = ScadaSOEModels
        fields = '__all__'
