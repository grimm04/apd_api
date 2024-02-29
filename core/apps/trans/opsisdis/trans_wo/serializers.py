from email.policy import default
from numpy import source
from rest_framework import serializers
import datetime
from apps.users.models import Users
from .models import TransWo
from apps.master.opsisdis.wo.ref_wo_jenis.models import RefWOJenis 
from apps.master.opsisdis.wo.ref_wo_jenis.serializers import RefWOJenisGetSerializer 

class GetTransWoSerializers(serializers.ModelSerializer): 
    ref_wo_jenis = RefWOJenisGetSerializer(source='id_ref_wo_jenis')
    
    class Meta:
        model = TransWo
        fields = '__all__'

class CRTransWoSerializers(serializers.ModelSerializer): 
    nomor = serializers.CharField(default=None, max_length=100, allow_null=True, allow_blank=True)
    uraian = serializers.CharField(default=None, max_length=100, allow_null=True, allow_blank=True) 
    id_pelaksana = serializers.IntegerField(default=None, allow_null=True)
    id_station = serializers.IntegerField(default=None, allow_null=True)

    id_ref_wo_jenis = serializers.SlugRelatedField(
        queryset=RefWOJenis.objects.all(),
        slug_field='id_ref_wo_jenis',
        allow_null=False,
        style={'base_template': 'input.html'}
    )
    # id_wo_log_status = serializers.SlugRelatedField(
    #     queryset=TransWoLogStatus.objects.all(),
    #     slug_field='id_wo_log_status',
    #     allow_null=False,
    #     style={'base_template': 'input.html'}
    # )

    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        style={'base_template': 'input.html'}
    )
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True, 
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_wo_jenis = RefWOJenisGetSerializer(read_only=True,source='id_ref_wo_jenis')
    tgl_mulai = serializers.DateField(default=None, required=False,  allow_null=True)
    tgl_selesai = serializers.DateField(default=None, required=False,  allow_null=True)
    tgl_entri = serializers.DateField(format="%Y-%m-%d", read_only=True)
    tgl_update = serializers.DateField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = TransWo
        fields = '__all__'


class UDTransWoSerializers(serializers.ModelSerializer):
    queryset = TransWo.objects.all() 

    nomor = serializers.CharField(max_length=100, allow_null=True, allow_blank=True, required=False)
    uraian = serializers.CharField(max_length=100, allow_null=True, allow_blank=True, required=False) 
    id_pelaksana = serializers.IntegerField(allow_null=True, required=False)
    id_station = serializers.IntegerField(allow_null=True, required=False)

    id_ref_wo_jenis = serializers.SlugRelatedField(
        queryset=RefWOJenis.objects.all(),
        slug_field='id_ref_wo_jenis',
        allow_null=False,
        required=False,
        style={'base_template': 'input.html'}
    )
    # id_wo_log_status = serializers.SlugRelatedField(
    #     queryset=TransWoLogStatus.objects.all(),
    #     slug_field='id_wo_log_status',
    #     allow_null=False,
    #     required=False,
    #     style={'base_template': 'input.html'}
    # )

    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=False,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True, 
        required=True,
        style={'base_template': 'input.html'}
    )
    tgl_mulai = serializers.DateField(default=None, required=False,allow_null=True)
    tgl_selesai = serializers.DateField(default=None, required=False,allow_null=True)

    class Meta:
        model = TransWo
        fields = '__all__'

 