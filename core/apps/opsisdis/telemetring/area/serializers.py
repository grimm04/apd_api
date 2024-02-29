from rest_framework import serializers
from .models import TelemetringArea
from apps.master.jaringan.ref_lokasi.models import RefLokasi
from apps.users.models import Users
from datetime import datetime
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from apps.additional.serializers import IDSRef_LokasiSerializer , SubRefParentLokasiSerializer 
 

class SubUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['fullname', 'nip', 'gender']

@extend_schema_serializer(
    exclude_fields=('id_trans_tm_area', 'tgl_entri', 'tgl_update'),
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
                    # "f": 5,
                    "id_lokasi": 112,
                    "id_user_entri": 1,
                    "id_user_update": 1
                },
                {
                    "datum": datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'),
                    "i": 6,
                    "v": 7,
                    "p": 8,
                    "q": 9,
                    # "f": 10,
                    "id_lokasi": 113,
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
                    # "f": 5,
                    "id_lokasi": 112,
                    "id_user_entri": 1,
                    "id_user_update": 1
                },
            request_only=True,
            response_only=False,
        ),
    ]
)
class TelemetringAreaSerializers(serializers.ModelSerializer):
    datum = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S.%f", read_only=True)
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
    ref_parent_lokasi = SubRefParentLokasiSerializer(read_only=True, source='id_lokasi.id_parent_lokasi')
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
        model = TelemetringArea
        fields = '__all__'

@extend_schema_serializer(
    exclude_fields=('id_trans_tm_area', 'tgl_entri', 'tgl_update'),
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
                    "id_trans_tm_area": 1,
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
                    "id_trans_tm_area": 2,
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
                    "datum": datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'),
                    "i": 1,
                    "v": 2,
                    "p": 3,
                    "q": 4,
                    # "f": 5,
                    "id_lokasi": 112,
                    "id_trans_tm_area": 1,
                    "id_user_update": 1
                },
            request_only=True,
            response_only=False,
        ),
    ]
)
class UDTelemetringAreaSerializers(serializers.ModelSerializer):
    i = serializers.IntegerField(default=None, allow_null=True)
    v = serializers.IntegerField(default=None, allow_null=True)
    p = serializers.IntegerField(default=None, allow_null=True)
    q = serializers.IntegerField(default=None, allow_null=True)
    # f = serializers.IntegerField(default=None, allow_null=True)

    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    user_update = SubUsersSerializer(read_only=True, source='id_user_update')

    class Meta:
        model = TelemetringArea
        fields = '__all__'