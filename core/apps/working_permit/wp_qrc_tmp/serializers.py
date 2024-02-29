from rest_framework import serializers

from .models import WP_QRC_TMP 
from apps.working_permit.wp_qrc.models import WP_QRC 
from apps.master.working_permit.pertanyaan_qrc.models import PertanyaanQRC




 
class PertanyaanQRCSerializer(serializers.ModelSerializer):

    class Meta:
        model = PertanyaanQRC
        fields = ['id_pertanyaan_qrc', 'pertanyaan_qrc','pertanyaan_qrc_point']


class WP_QRC_TMPSerializers(serializers.ModelSerializer): 
    ada = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)  
    id_pertanyaan_qrc = serializers.SlugRelatedField(
        queryset=PertanyaanQRC.objects.all(),
        slug_field='id_pertanyaan_qrc',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )   
    pertanyaan_qrc = PertanyaanQRCSerializer(read_only=True, source='id_pertanyaan_qrc') 
    

    class Meta:
        model = WP_QRC_TMP
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
                    "id_WP_QRC_TMP": 0,
                    "ada": 1, 
                    "id_pertanyaan_qrc": 0
                },
                { 
                    "id_WP_QRC_TMP": 0,
                    "ada": 1, 
                    "id_pertanyaan_qrc": 0
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
                    "id_WP_QRC_TMP": 0,
                    "ada": 1, 
                    "id_pertanyaan_qrc": 0
                }, 
            request_only=True, 
            response_only=False,
        ),
    ]
)
class CDWP_QRC_TMPSerializers(serializers.ModelSerializer):

    ada = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    id_pertanyaan_qrc = serializers.SlugRelatedField(
        queryset=PertanyaanQRC.objects.all(),
        slug_field='id_pertanyaan_qrc',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )  

    class Meta:
        model = WP_QRC_TMP
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
                    "id_WP_QRC_TMP": 0,
                    "ada": 1, 
                    "id_pertanyaan_qrc": 0
                },
                { 
                    "id_WP_QRC_TMP": 0,
                    "ada": 1, 
                    "id_pertanyaan_qrc": 0
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
                    "id_WP_QRC_TMP": 0,
                    "ada": 1, 
                    "id_pertanyaan_qrc": 0
                }, 
            request_only=True, 
            response_only=False,
        ),
    ]
)
class UDWP_QRC_TMPSerializers(serializers.ModelSerializer):
    ada = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)  
    id_pertanyaan_qrc = serializers.SlugRelatedField(
        queryset=PertanyaanQRC.objects.all(),
        slug_field='id_pertanyaan_qrc',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )  
    class Meta:
        model = WP_QRC_TMP
        fields = '__all__'

