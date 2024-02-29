from rest_framework import serializers

from apps.users.models import Users
from .models import RefAsetJenisMutasi

class RefAsetJenisMutasiSerializersList(serializers.ModelSerializer):
    # user_entri = UserDetailSerializerDef(read_only=True, source='id_user_entri')
    class Meta:
        model = RefAsetJenisMutasi
        fields = '__all__'
class CRRefAsetJenisMutasiSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=100)
    status = serializers.IntegerField(default=None, allow_null=True) 

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
        model = RefAsetJenisMutasi
        fields = '__all__'


class UDRefAsetJenisMutasiSerializers(serializers.ModelSerializer):
    queryset = RefAsetJenisMutasi.objects.all()

    nama = serializers.CharField(max_length=100)
    status = serializers.IntegerField(required=False)

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
        model = RefAsetJenisMutasi
        fields = '__all__'

 