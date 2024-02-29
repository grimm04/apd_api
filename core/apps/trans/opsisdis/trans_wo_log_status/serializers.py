from rest_framework import serializers

from apps.users.models import Users
from .models import TransWoLogStatus
from apps.master.opsisdis.wo.ref_wo_status.models import RefWOStatus
from apps.trans.opsisdis.trans_wo.models import TransWo

from apps.master.opsisdis.wo.ref_wo_status.serializers import RefWOStatusGetSerializer

class CRTransWoLogStatusSerializers(serializers.ModelSerializer): 
    id_wo = serializers.SlugRelatedField(
        queryset=TransWo.objects.all(),
        slug_field='id_wo',
        allow_null=False,
        required=True,
        style={'base_template': 'input.html'}
    )
    id_ref_wo_status = serializers.SlugRelatedField(
        queryset=RefWOStatus.objects.all(),
        slug_field='id_ref_wo_status',
        allow_null=False,
        style={'base_template': 'input.html'}
    )

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
    ref_wo_status = RefWOStatusGetSerializer(read_only=True, source='id_ref_wo_status')
    tgl_entri = serializers.DateField(format="%Y-%m-%d", read_only=True)
    tgl_update = serializers.DateField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = TransWoLogStatus
        fields = '__all__'


class UDTransWoLogStatusSerializers(serializers.ModelSerializer):
    queryset = TransWoLogStatus.objects.all() 
    id_wo = serializers.SlugRelatedField(
        queryset=TransWo.objects.all(),
        slug_field='id_wo',
        allow_null=False,
        required=True,
        style={'base_template': 'input.html'}
    )

    id_ref_wo_status = serializers.SlugRelatedField(
        queryset=RefWOStatus.objects.all(),
        slug_field='id_ref_wo_status',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
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

    class Meta:
        model = TransWoLogStatus
        fields = '__all__'

 