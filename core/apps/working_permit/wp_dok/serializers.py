from rest_framework import serializers

from apps.working_permit.wp_online.models import WP_ONLINE
from .models import WP_DOK  
from datetime import datetime 

class WP_DOKSerializers(serializers.ModelSerializer):  
    nama_dok = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)  
   
    id_wp_online = serializers.SlugRelatedField(
        queryset=WP_ONLINE.objects.all(),
        slug_field='id_wp_online',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )   
    tgl_entri = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M:%S" )

    class Meta:
        model = WP_DOK
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
                    "id_wp_dok": 0,
                    "nama_dok": "string",
                    "id_wp_online": 0,
                    "tgl_entri": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                }, 
                 { 
                    "id_wp_dok": 0,
                    "nama_dok": "string",
                    "id_wp_online": 0,
                    "tgl_entri": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
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
                    "id_wp_dok": 0,
                    "nama_dok": "string",
                    "id_wp_online": 0,
                    "tgl_entri": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                }, 
            request_only=True, 
            response_only=False,
        ),
    ]
)
class CDWP_DOKSerializers(serializers.ModelSerializer):

    nama_dok = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)  
   
    id_wp_online = serializers.SlugRelatedField(
        queryset=WP_ONLINE.objects.all(),
        slug_field='id_wp_online',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )   
    tgl_entri = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M:%S" ) 

    class Meta:
        model = WP_DOK
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
                    "id_wp_dok": 0,
                    "nama_dok": "string",
                    "id_wp_online": 0,
                    "tgl_entri": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                }, 
                { 
                    "id_wp_dok": 0,
                    "nama_dok": "string",
                    "id_wp_online": 0,
                    "tgl_entri": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
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
                    "id_wp_dok": 0,
                    "nama_dok": "string",
                    "id_wp_online": 0,
                    "tgl_entri": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                }, 
            request_only=True, 
            response_only=False,
        ),
    ]
)
class UDWP_DOKSerializers(serializers.ModelSerializer):
    nama_dok = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)  
   
    id_wp_online = serializers.SlugRelatedField(
        queryset=WP_ONLINE.objects.all(),
        slug_field='id_wp_online',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )   
    tgl_entri = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M:%S" ) 
    class Meta:
        model = WP_DOK
        fields = '__all__'

