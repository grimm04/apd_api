from rest_framework import serializers

from .models import WP_HIRARC_DETAIL 
from apps.working_permit.wp_hirarc.models import WP_HIRARC


 
class WP_HIRARCSerializer(serializers.ModelSerializer):

    class Meta:
        model = WP_HIRARC
        fields = ['id_wp_hirarc', 'name']


class WP_HIRARC_DETAILSerializers(serializers.ModelSerializer): 
    kegiatan = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    bahaya = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    resiko_bahaya = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    peluang = serializers.CharField(max_length=20, allow_blank=True, allow_null=True) 
    akibat = serializers.CharField(max_length=20, allow_blank=True, allow_null=True) 
    tingkat_resiko = serializers.CharField(max_length=20, allow_blank=True, allow_null=True) 
    pengendalian = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    penanggung_jawab = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    peluang2 = serializers.CharField(max_length=20) 
    akibat2 = serializers.CharField(max_length=20) 
    tingkat_resiko2 = serializers.CharField(max_length=20)
    status_pengendalian = serializers.BooleanField(default=True)
    id_wp_hirarc = serializers.SlugRelatedField(
        queryset=WP_HIRARC.objects.all(),
        slug_field='id_wp_hirarc',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    ) 

    class Meta:
        model = WP_HIRARC_DETAIL
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
                    "id_wp_hirarc": 1,
                    "kegiatan": "string",
                    "bahaya": "string", 
                    "resiko_bahaya": "string", 
                    "peluang": "string", 
                    "akibat": "string", 
                    "tingkat_resiko": "string", 
                    "pengendalian": "string", 
                    "penganggung_jawab": "string"
                },
                { 
                    "id_wp_hirarc": 1,
                    "kegiatan": "string",
                    "bahaya": "string", 
                    "resiko_bahaya": "string", 
                    "peluang": "string", 
                    "akibat": "string", 
                    "tingkat_resiko": "string", 
                    "pengendalian": "string", 
                    "penganggung_jawab": "string"
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
                    "id_wp_hirarc": 1,
                    "kegiatan": "string",
                    "bahaya": "string", 
                    "resiko_bahaya": "string", 
                    "peluang": "string", 
                    "akibat": "string", 
                    "tingkat_resiko": "string", 
                    "pengendalian": "string", 
                    "penganggung_jawab": "string"
                },
            request_only=True, 
            response_only=False,
        ),
    ]
)
class CDWP_HIRARC_DETAILSerializers(serializers.ModelSerializer):

    kegiatan = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    bahaya = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    resiko_bahaya = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    peluang = serializers.CharField(max_length=20, allow_blank=True, allow_null=True) 
    akibat = serializers.CharField(max_length=20, allow_blank=True, allow_null=True) 
    tingkat_resiko = serializers.CharField(max_length=20, allow_blank=True, allow_null=True) 
    pengendalian = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    penganggung_jawab = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    peluang2 = serializers.CharField(max_length=20,required=False) 
    akibat2 = serializers.CharField(max_length=20,required=False) 
    tingkat_resiko2 = serializers.CharField(max_length=20,required=False)
    status_pengendalian = serializers.BooleanField(default=True)
    id_wp_hirarc = serializers.SlugRelatedField(
        queryset=WP_HIRARC.objects.all(),
        slug_field='id_wp_hirarc',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 


    class Meta:
        model = WP_HIRARC_DETAIL
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
                    "id_wp_hirarc_detail":1,
                    "id_wp_hirarc": 1,
                    "kegiatan": "string",
                    "bahaya": "string", 
                    "resiko_bahaya": "string", 
                    "peluang": "string", 
                    "akibat": "string", 
                    "tingkat_resiko": "string", 
                    "pengendalian": "string", 
                    "penganggung_jawab": "string"
                },
                {   
                    "id_wp_hirarc_detail":1,
                    "id_wp_hirarc": 1,
                    "kegiatan": "string",
                    "bahaya": "string", 
                    "resiko_bahaya": "string", 
                    "peluang": "string", 
                    "akibat": "string", 
                    "tingkat_resiko": "string", 
                    "pengendalian": "string", 
                    "penganggung_jawab": "string"
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
                    "id_wp_hirarc": 1,
                    "kegiatan": "string",
                    "bahaya": "string", 
                    "resiko_bahaya": "string", 
                    "peluang": "string", 
                    "akibat": "string", 
                    "tingkat_resiko": "string", 
                    "pengendalian": "string", 
                    "penganggung_jawab": "string"
                },
            request_only=True, 
            response_only=False,
        ),
    ]
)
class UDWP_HIRARC_DETAILSerializers(serializers.ModelSerializer):
    kegiatan = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    bahaya = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    resiko_bahaya = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    peluang = serializers.CharField(max_length=20, allow_blank=True, allow_null=True) 
    akibat = serializers.CharField(max_length=20, allow_blank=True, allow_null=True) 
    tingkat_resiko = serializers.CharField(max_length=20, allow_blank=True, allow_null=True) 
    pengendalian = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    penganggung_jawab = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    peluang2 = serializers.CharField(max_length=20,required=False) 
    akibat2 = serializers.CharField(max_length=20,required=False) 
    tingkat_resiko2 = serializers.CharField(max_length=20,required=False)
    status_pengendalian = serializers.BooleanField(default=True)
    id_wp_hirarc = serializers.SlugRelatedField(
        queryset=WP_HIRARC.objects.all(),
        slug_field='id_wp_hirarc',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 


    class Meta:
        model = WP_HIRARC_DETAIL
        fields = '__all__'

