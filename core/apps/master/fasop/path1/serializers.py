from rest_framework import serializers
from .models import FASOPPATH1
from apps.master.jaringan.ref_lokasi.models import RefLokasi


class SubRefLokasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi', 'nama_lokasi', 'kode_lokasi']


class FASOPPATH1Serializers(serializers.ModelSerializer):
    path1 = serializers.CharField(max_length=255, default=None, allow_blank=True, allow_null=True)
    status = serializers.IntegerField(default=None, allow_null=True)
    # datum_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    id_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_lokasi = SubRefLokasiSerializer(read_only=True, source='id_lokasi')

    class Meta:
        model = FASOPPATH1
        fields = '__all__'


class CRFASOPPATH1CSerializers(serializers.ModelSerializer):
    path1 = serializers.CharField(max_length=255, default=None, allow_blank=True, allow_null=True)
    status = serializers.IntegerField(default=None, allow_null=True)
    # datum_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    id_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    class Meta:
        model = FASOPPATH1
        fields = '__all__'


class UDFASOPPATH1Serializers(serializers.ModelSerializer):
    path1 = serializers.CharField(max_length=255, default=None, allow_blank=True, allow_null=True)
    status = serializers.IntegerField(default=None, allow_null=True)
    # datum_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    id_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    class Meta:
        model = FASOPPATH1
        fields = '__all__'
