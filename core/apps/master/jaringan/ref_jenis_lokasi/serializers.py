from rest_framework import serializers

from apps.users.models import Users
from .models import RefJenisLokasi


class RefJenisLokasierializer(serializers.ModelSerializer):
    class Meta:
        model = RefJenisLokasi
        fields = ['id_ref_jenis_lokasi', 'nama_jenis_lokasi']


class CRRefJenisLokasiSerializers(serializers.ModelSerializer):
    nama_jenis_lokasi = serializers.CharField(max_length=100)
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
        style={'base_template': 'input.html'}
    )
    tgl_entri = serializers.DateField(format="%Y-%m-%d", read_only=True)
    tgl_update = serializers.DateField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = RefJenisLokasi
        fields = '__all__'


class UDRefJenisLokasiSerializers(serializers.ModelSerializer):
    queryset = RefJenisLokasi.objects.all()

    nama_jenis_lokasi = serializers.CharField(max_length=100)
    # id_user_entri = serializers.SlugRelatedField(
    #     queryset=Users.objects.all(),
    #     slug_field='id_user',
    #     allow_null=True,
    #     style={'base_template': 'input.html'}
    # )
    # id_user_entri = serializers.ReadOnlyField()
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    class Meta:
        model = RefJenisLokasi
        fields = '__all__'
