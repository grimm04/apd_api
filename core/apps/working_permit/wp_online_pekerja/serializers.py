from rest_framework import serializers 
from apps.users.models import Users
from apps.working_permit.wp_online.models import WP_ONLINE
from apps.users.models import Users

from .models import WP_ONLINE_PEKERJA   
from apps.additional.serializers import UserDetailSerializerDef
 
class WP_ONLINE_PEKERJASerializers(serializers.ModelSerializer): 

    nama_pekerja = serializers.CharField(max_length=150, allow_blank=True, allow_null=True, default=None)  

    id_wp_online = serializers.SlugRelatedField(
        queryset=WP_ONLINE.objects.all(),
        slug_field='id_wp_online',
        allow_null=True,
        style={'base_template': 'input.html'}
    )
     
    
    class Meta:
        model = WP_ONLINE_PEKERJA
        fields = '__all__'

from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
@extend_schema_serializer(
    exclude_fields=[], # schema ignore these fields
    examples = [
         OpenApiExample(
            'Batch Example',
            summary='Batch Example',
            description='Batch Example',
            value=[
                { 
                    "id_wp_online_pekerja": 0,
                    "nama_pekerja": "string",
                    "id_wp_online": 0
                },
                { 
                   "id_wp_online_pekerja": 0,
                    "nama_pekerja": "string",
                    "id_wp_online": 0
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
                    "id_wp_online_pekerja": 0,
                    "nama_pekerja": "string",
                    "id_wp_online": 0 
                }, 
            request_only=True, 
            response_only=False,
        ),
    ]
)
class CDWP_ONLINE_PEKERJASerializers(serializers.ModelSerializer):

    nama_pekerja = serializers.CharField(max_length=150, allow_blank=True, allow_null=True, default=None)  

    id_wp_online = serializers.SlugRelatedField(
        queryset=WP_ONLINE.objects.all(),
        slug_field='id_wp_online',
        allow_null=True,
        style={'base_template': 'input.html'}
    ) 


    class Meta:
        model = WP_ONLINE_PEKERJA
        fields = '__all__'  

@extend_schema_serializer(
    exclude_fields=[], # schema ignore these fields
    examples = [
         OpenApiExample(
            'Batch Example',
            summary='Batch Example',
            description='Batch Example',
            value=[
                { 
                   "id_wp_online_pekerja": 0,
                    "nama_pekerja": "string",
                    "id_wp_online": 0
                },
                { 
                   "id_wp_online_pekerja": 0,
                    "nama_pekerja": "string",
                    "id_wp_online": 0 
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
                   "id_wp_online_pekerja": 0,
                    "nama_pekerja": "string",
                    "id_wp_online": 0 
                }, 
            request_only=True, 
            response_only=False,
        ),
    ]
)
class UDWP_ONLINE_PEKERJASerializers(serializers.ModelSerializer):
    nama_pekerja = serializers.CharField(max_length=150, allow_blank=True, allow_null=True, default=None)  

    id_wp_online = serializers.SlugRelatedField(
        queryset=WP_ONLINE.objects.all(),
        slug_field='id_wp_online',
        allow_null=True,
        style={'base_template': 'input.html'}
    )
    

    class Meta:
        model = WP_ONLINE_PEKERJA
        fields = '__all__'