from rest_framework import serializers
 
from apps.users.models import Users

from .models import WP_QRC  

 

class WP_QRCSerializers(serializers.ModelSerializer):
    nama_user = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    nama_pekerjaan = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    vendor = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    key_qrc = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)  

    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    tgl_entri = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None) 
    tgl_update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None)  
    class Meta:
        model = WP_QRC
        fields = '__all__'



from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
@extend_schema_serializer(
    exclude_fields=['tgl_entri','tgl_update'], # schema ignore these fields
    examples = [
         OpenApiExample(
            'Batch Example',
            summary='Batch Example',
            description='Batch Example',
            value=[
                {   
                    "nama_user": "string",
                    "nama_pekerjaan": "string",
                    "vendor": "string",
                    "key_qrc": "string",
                    "id_user_entri": "string",
                    "id_user_update": "string",
                    "tgl_entri": "2022-05-11 13:00:00",
                    "tgl_update": "2022-05-11 13:00:00" 
                },
                {   
                    "nama_user": "string",
                    "nama_pekerjaan": "string",
                    "vendor": "string",
                    "key_qrc": "string",
                    "id_user_entri": "string",
                    "id_user_update": "string",
                    "tgl_entri": "2022-05-11 13:00:00",
                    "tgl_update": "2022-05-11 13:00:00" 
                },
                 
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
                    "nama_user": "string",
                    "nama_pekerjaan": "string",
                    "vendor": "string",
                    "key_qrc": "string",
                    "id_user_entri": "string",
                    "id_user_update": "string",
                    "tgl_entri": "2022-05-11 13:00:00",
                    "tgl_update": "2022-05-11 13:00:00" 
                }, 
            request_only=True, 
            response_only=False,
        ),
    ]
)
class CDWP_QRCSerializers(serializers.ModelSerializer):

    nama_user = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    nama_pekerjaan = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    vendor = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    key_qrc = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)  

    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    tgl_entri = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None) 
    tgl_update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None)  

    class Meta:
        model = WP_QRC
        fields = '__all__' 

@extend_schema_serializer(
    exclude_fields=['tgl_entri','tgl_update'], # schema ignore these fields
    examples = [
         OpenApiExample(
            'Batch Example',
            summary='Batch Example',
            description='Batch Example',
            value=[
                {  
                    "id_wp_qrc": 0,
                    "nama_user": "string",
                    "nama_pekerjaan": "string",
                    "vendor": "string",
                    "key_qrc": "string",
                    "id_user_entri": "string",
                    "id_user_update": "string",
                    "tgl_entri": "2022-05-11 13:00:00",
                    "tgl_update": "2022-05-11 13:00:00" 
                },
                {  
                    "id_wp_qrc": 0,
                    "nama_user": "string",
                    "nama_pekerjaan": "string",
                    "vendor": "string",
                    "key_qrc": "string",
                    "id_user_entri": "string",
                    "id_user_update": "string",
                    "tgl_entri": "2022-05-11 13:00:00",
                    "tgl_update": "2022-05-11 13:00:00" 
                },
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
                    "id_WP_QRC":1,
                    "id_wp_master_bagian": 1,
                    "pekerjaan": "string",
                    "lokasi_pekerjaan": "string",
                    "tanggal": '2022-05-11 13:00'
                },
            request_only=True, 
            response_only=False,
        ),
    ]
)
class UDWP_QRCSerializers(serializers.ModelSerializer):
    nama_user = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    nama_pekerjaan = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    vendor = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    key_qrc = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)  

    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
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

    tgl_entri = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None) 
    tgl_update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None)  

    class Meta:
        model = WP_QRC
        fields = '__all__'

