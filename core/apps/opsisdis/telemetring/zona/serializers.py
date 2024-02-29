from rest_framework import serializers
from .models import TelemetringZona
from apps.master.jaringan.ref_lokasi.models import RefLokasi
from apps.users.models import Users
from datetime import datetime
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from apps.additional.serializers import IDSRef_LokasiSerializer,SubRefParentLokasiSerializer 
  

class SubUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['fullname', 'nip', 'gender']

@extend_schema_serializer(
    exclude_fields=('id_trans_tm_zona', 'tgl_entri', 'tgl_update'),
    examples=[
         OpenApiExample(
            'Batch Example',
            summary='Batch Example',
            description='Batch Example',
            value=[
                {
                    "datum": datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'),
                    "i": 1,
                    "v": 2,
                    "p": 3,
                    "q": 4,
                    "f": 5,
                    "id_lokasi": 112,
                    "id_parent_lokasi": 1,
                    "id_user_entri": 1,
                    "id_user_update": 1
                },
                {
                    "datum": datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'),
                    "i": 6,
                    "v": 7,
                    "p": 8,
                    "q": 9,
                    "f": 10,
                    "id_lokasi": 113,
                    "id_parent_lokasi": 1,
                    "id_user_entri": 13,
                    "id_user_update": 13
                }
            ],
            request_only=True,
            response_only=False,
        ),
         OpenApiExample(
            'Single Example',
            summary='Single Example',
            description='Single Example',
            value=
                {
                    "datum": datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'),
                    "i": 1,
                    "v": 2,
                    "p": 3,
                    "q": 4,
                    "f": 5,
                    "id_lokasi": 112,
                    "id_parent_lokasi": 1,
                    "id_user_entri": 1,
                    "id_user_update": 1
                },
            request_only=True,
            response_only=False,
        ),
    ]
)
class TelemetringZonaSerializers(serializers.ModelSerializer):
    datum = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    i = serializers.IntegerField(default=None, allow_null=True)
    v = serializers.IntegerField(default=None, allow_null=True)
    p = serializers.IntegerField(default=None, allow_null=True)
    q = serializers.IntegerField(default=None, allow_null=True)
    f = serializers.IntegerField(default=None, allow_null=True)
    id_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_lokasi = IDSRef_LokasiSerializer(read_only=True, source='id_lokasi')
    id_parent_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_parent_lokasi = SubRefParentLokasiSerializer(read_only=True, source='id_parent_lokasi')
    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        style={'base_template': 'input.html'}
    )
    user_entri = SubUsersSerializer(read_only=True, source='id_user_entri')
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    user_update = SubUsersSerializer(read_only=True, source='id_user_update')

    class Meta:
        model = TelemetringZona
        fields = '__all__'

@extend_schema_serializer(
    exclude_fields=('id_trans_tm_zona', 'tgl_entri', 'tgl_update'),
    examples=[
         OpenApiExample(
            'Batch Example',
            summary='Batch Example',
            description='Batch Example',
            value=[
                {
                    "i": 1,
                    "v": 2,
                    "p": 3,
                    "q": 4,
                    "f": 5,
                    "id_trans_tm_zona": 1,
                    "id_user_update": 1
                },
                {
                    "i": 6,
                    "v": 7,
                    "p": 8,
                    "q": 9,
                    "f": 10,
                    "id_trans_tm_zona": 2,
                    "id_user_update": 5
                }
            ],
            request_only=True,
            response_only=False,
        ),
         OpenApiExample(
            'Single Example',
            summary='Single Example',
            description='Single Example',
            value=
                {
                    "i": 1,
                    "v": 2,
                    "p": 3,
                    "q": 4,
                    "f": 5,
                    "id_trans_tm_zona": 1,
                    "id_user_update": 1
                },
            request_only=True,
            response_only=False,
        ),
    ]
)
class UDTelemetringZonaSerializers(serializers.ModelSerializer):
    i = serializers.IntegerField(default=None, allow_null=True)
    v = serializers.IntegerField(default=None, allow_null=True)
    p = serializers.IntegerField(default=None, allow_null=True)
    q = serializers.IntegerField(default=None, allow_null=True)
    f = serializers.IntegerField(default=None, allow_null=True)

    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    user_update = SubUsersSerializer(read_only=True, source='id_user_update')

    class Meta:
        model = TelemetringZona
        fields = '__all__'

class ByTelemetringZonaSerializers(serializers.ModelSerializer):

    id_lokasi = serializers.SerializerMethodField('get_id_lokasi')

    def get_id_lokasi(self, obj):
        id_lokasi = TelemetringZona.objects.filter(id_lokasi=obj['id_lokasi'])
        serializer = TelemetringZonaSerializers(id_lokasi, many=True)
        return serializer.data

    class Meta:
        model = TelemetringZona
        fields = ('id_lokasi', 'datum')

@extend_schema_serializer(
    exclude_fields=('id_trans_tm_zona', 'tgl_entri', 'tgl_update'),
    examples=[
         OpenApiExample(
            'Single Example',
            summary='Single Example',
            description='Single Example',
            value=
                {
                    "id_user_entri": 1,
                    "id_parent_lokasi": 1,
                    "datum": datetime.today().strftime('%Y-%m-%d')
                },
            request_only=True,
            response_only=False,
        ),
    ]
)
class TelemetringZonaGenerateSerializers(serializers.Serializer):
    id_parent_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        style={'base_template': 'input.html'} 
    )
    # datum = serializers.DateTimeField(required=True)

    # class Meta:
    #     model = TelemetringZona
    #     fields = '__all__'