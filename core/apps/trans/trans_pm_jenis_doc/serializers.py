from rest_framework import serializers

from apps.users.models import Users
from .models import TransPmJenisDoc


class CRTransPmJenisDocSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=100) 

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
    tgl_entri = serializers.DateField(format="%Y-%m-%d", read_only=True)
    tgl_update = serializers.DateField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = TransPmJenisDoc
        fields = '__all__'


class UDTransPmJenisDocSerializers(serializers.ModelSerializer):
    queryset = TransPmJenisDoc.objects.all()

    nama = serializers.CharField(max_length=100,required=True) 

    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=False,
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
        model = TransPmJenisDoc
        fields = '__all__'

 