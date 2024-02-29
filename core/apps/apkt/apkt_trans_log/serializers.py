from rest_framework import serializers
from .models import APKTTransLog
from apps.apkt.apkt_trans_jar.models import APKTTransJAR
from apps.users.models import Users

class SubAPKTTransJARSerializer(serializers.ModelSerializer):

    class Meta:
        model = APKTTransJAR
        fields = '__all__'

class APKTTransLogSerializers(serializers.ModelSerializer):
    id_apkt_trans_jar = serializers.SlugRelatedField(
        queryset=APKTTransJAR.objects.all(),
        slug_field='id_apkt_trans_jar',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_apkt_trans_jar = SubAPKTTransJARSerializer(read_only=True, source='id_apkt_trans_jar')
    tgl_mulai = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_selesai = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_buat = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    input_apkt = serializers.CharField(max_length=4000, default=None, allow_blank=True, allow_null=True)
    output_apkt = serializers.CharField(max_length=4000, default=None, allow_blank=True, allow_null=True)
    server_apkt = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    webservice = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)

    class Meta:
        model = APKTTransLog
        fields = '__all__'

class UDAPKTTransLogSerializers(serializers.ModelSerializer):
    id_apkt_trans_jar = serializers.SlugRelatedField(
        queryset=APKTTransJAR.objects.all(),
        slug_field='id_apkt_trans_jar',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_apkt_trans_jar = SubAPKTTransJARSerializer(read_only=True, source='id_apkt_trans_jar')
    tgl_mulai = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_selesai = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_buat = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    input_apkt = serializers.CharField(max_length=4000, default=None, allow_blank=True, allow_null=True)
    output_apkt = serializers.CharField(max_length=4000, default=None, allow_blank=True, allow_null=True)
    server_apkt = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    webservice = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)

    class Meta:
        model = APKTTransLog
        fields = '__all__'