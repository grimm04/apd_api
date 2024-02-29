from rest_framework import serializers

from .models import ExtUserTokenRole
from apps.external.ext_user_token.models import ExtUserToken
from apps.external.ext_module.models import ExtModule


class SubExtUserTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtUserToken
        fields = ['id_token', 'nama', 'created_at']


class SubExtModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtModule
        fields = ['id_module', 'nama']


class ExtUserTokenRoleSerializers(serializers.ModelSerializer):
    id_token = serializers.SlugRelatedField(
        queryset=ExtUserToken.objects.all(),
        slug_field='id_token',
        allow_null=False,
        required=True,
        style={'base_template': 'input.html'}
    )
    ext_user_token = SubExtUserTokenSerializer(read_only=True, source='id_token')
    id_module = serializers.SlugRelatedField(
        queryset=ExtModule.objects.all(),
        slug_field='id_module',
        allow_null=False,
        required=True,
        style={'base_template': 'input.html'}
    )
    ext_module = SubExtModuleSerializer(read_only=True, source='id_module')

    class Meta:
        model = ExtUserTokenRole
        fields = '__all__'
