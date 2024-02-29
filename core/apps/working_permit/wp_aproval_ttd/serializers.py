from rest_framework import serializers  

from .models import WP_APROVAL_TTD   
from apps.master.working_permit.wm_bagian.models import WP_BAGIAN

from apps.users.models import Users
 
class WP_APROVAL_TTDSerializers(serializers.ModelSerializer):  
    id_user = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        style={'base_template': 'input.html'}
    )
    id_wp_master_bagian = serializers.SlugRelatedField(
        queryset=WP_BAGIAN.objects.all(),
        slug_field='id_wp_master_bagian',
        allow_null=True,
        style={'base_template': 'input.html'}
    )
     
    
    class Meta:
        model = WP_APROVAL_TTD
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
                    "id_wp_aproval_ttd": 0, 
                    "id_user": 0, 
                    "id_wp_master_bagian": 0 
                }, 
               { 
                    "id_wp_aproval_ttd": 0, 
                    "id_user": 0, 
                    "id_wp_master_bagian": 0 
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
                    "id_wp_aproval_ttd": 0, 
                    "id_user": 0, 
                    "id_wp_master_bagian": 0 
                }, 
            request_only=True, 
            response_only=False,
        ),
    ]
)
class CDWP_APROVAL_TTDSerializers(serializers.ModelSerializer):

    id_user = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    id_wp_master_bagian = serializers.SlugRelatedField(
        queryset=WP_BAGIAN.objects.all(),
        slug_field='id_wp_master_bagian',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )


    class Meta:
        model = WP_APROVAL_TTD
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
                    "id_wp_aproval_ttd": 0, 
                    "id_user": 0, 
                    "id_wp_master_bagian": 0 
                }, 
                { 
                    "id_wp_aproval_ttd": 0, 
                    "id_user": 0, 
                    "id_wp_master_bagian": 0 
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
                    "id_wp_aproval_ttd": 0, 
                    "id_user": 0, 
                    "id_wp_master_bagian": 0 
                }, 
            request_only=True, 
            response_only=False,
        ),
    ]
)
class UDWP_APROVAL_TTDSerializers(serializers.ModelSerializer): 
    id_user = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    id_wp_master_bagian = serializers.SlugRelatedField(
        queryset=WP_BAGIAN.objects.all(),
        slug_field='id_wp_master_bagian',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    

    class Meta:
        model = WP_APROVAL_TTD
        fields = '__all__'