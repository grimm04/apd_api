from rest_framework import serializers

from .models import WP_HIRARC 
from apps.master.working_permit.wm_bagian.models import WP_BAGIAN


from apps.additional.serializers import WP_BAGIANSerializer
from apps.working_permit.wp_hirarc_detail.serializers import WP_HIRARC_DETAILSerializers


class WP_HIRARCSerializers(serializers.ModelSerializer):
    pekerjaan = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
    lokasi_pekerjaan = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    tanggal = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None) 
    id_wp_master_bagian = serializers.SlugRelatedField(
        queryset=WP_BAGIAN.objects.all(),
        slug_field='id_wp_master_bagian',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    bagian = WP_BAGIANSerializer(read_only=True, source='id_wp_master_bagian') 

    class Meta:
        model = WP_HIRARC
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
                    "id_wp_master_bagian": 1,
                    "pekerjaan": "string",
                    "lokasi_pekerjaan": "string",
                    "tanggal": '2022-05-11 13:00'
                },
                { 
                    "id_wp_master_bagian": 1,
                    "pekerjaan": "string",
                    "lokasi_pekerjaan": "string",
                    "tanggal": '2022-05-11 13:00'
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
class CDWP_HIRARCSerializers(serializers.ModelSerializer):

    pekerjaan = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
    lokasi_pekerjaan = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    tanggal = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None) 
    id_wp_master_bagian = serializers.SlugRelatedField(
        queryset=WP_BAGIAN.objects.all(),
        slug_field='id_wp_master_bagian',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    ) 

    class Meta:
        model = WP_HIRARC
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
                    "id_wp_hirarc":1,
                    "id_wp_master_bagian": 1,
                    "pekerjaan": "string",
                    "lokasi_pekerjaan": "string",
                    "tanggal": '2022-05-11 13:00'
                },
                { 
                    "id_wp_master_bagian": 1,
                    "pekerjaan": "string",
                    "lokasi_pekerjaan": "string",
                    "tanggal": '2022-05-11 13:00'
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
                    "id_wp_hirarc":1,
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
class UDWP_HIRARCSerializers(serializers.ModelSerializer):
    pekerjaan = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
    lokasi_pekerjaan = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    tanggal = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None) 
    id_wp_master_bagian = serializers.SlugRelatedField(
        queryset=WP_BAGIAN.objects.all(),
        slug_field='id_wp_master_bagian',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    class Meta:
        model = WP_HIRARC
        fields = '__all__'


class Generate_HIRARCSerializers(serializers.ModelSerializer):
    pekerjaan = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
    lokasi_pekerjaan = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    tanggal = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None) 
    id_wp_master_bagian = serializers.SlugRelatedField(
        queryset=WP_BAGIAN.objects.all(),
        slug_field='id_wp_master_bagian',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    bagian = WP_BAGIANSerializer(read_only=True, source='id_wp_master_bagian')   
    hirarc_detail = WP_HIRARC_DETAILSerializers(many=True, read_only=True)
    class Meta:
        model = WP_HIRARC
        fields = '__all__'
        depth = 1