from rest_framework import serializers

from apps.users.models import Users
from .models import RefWOJenis


class RefWOJenisGetSerializer(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=100)
    status = serializers.IntegerField(default=None, allow_null=True) 
    kode = serializers.CharField(max_length=100)

    class Meta:
        model = RefWOJenis
        fields = ['nama','status','kode']

class CRRefWOJenisSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=100)
    status = serializers.IntegerField(default=None, allow_null=True)  
    kode = serializers.CharField(max_length=100)

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
        model = RefWOJenis
        fields = '__all__'


class UDRefWOJenisSerializers(serializers.ModelSerializer):
    queryset = RefWOJenis.objects.all()

    nama = serializers.CharField(max_length=100)
    status = serializers.IntegerField(default=None, allow_null=True)  
    kode = serializers.CharField(max_length=100)

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

    class Meta:
        model = RefWOJenis
        fields = '__all__'

 