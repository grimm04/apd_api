from rest_framework import serializers

from .models import ExtUserToken
from apps.users.models import Users


class SubUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['id_user', 'fullname', 'username', 'is_superuser']


class ExtUserTokenSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=100)
    token = serializers.CharField(max_length=150)
    id_user = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    user = SubUserSerializer(read_only=True, source='id_user')
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=None)

    class Meta:
        model = ExtUserToken
        fields = '__all__'


class UpdateExtUserTokenSerializers(serializers.ModelSerializer):
    token = serializers.CharField(max_length=999999999999)

    class Meta:
        model = ExtUserToken
        fields = ['token']
