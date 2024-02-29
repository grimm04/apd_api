from pickle import TRUE
from rest_framework import serializers

from apps.users.models import Users 
from apps.master.aset.ref_aset.models import RefAset

from .models import RefAsetExtAtr
from apps.master.aset.ref_aset_ex_atr.models import RefAsetExAtr

from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
@extend_schema_serializer(
    exclude_fields=('id_ref_aset_ext_atr','tgl_entri','tgl_update'), # schema ignore these fields
    examples = [
         OpenApiExample(
            'Batch Example',
            summary='Batch Example',
            description='Batch Example',
            value=[
                { 
                    "nilai": "string",
                    "status": 1,
                    "id_ref_aset": 0,
                    "id_ref_aset_ex_atr": 0
                },
                { 
                    "nilai": "string",
                    "status": 1,
                    "id_ref_aset": 0,
                    "id_ref_aset_ex_atr": 0
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
                    "nilai": "string",
                    "status": 1,
                    "id_ref_aset": 0,
                    "id_ref_aset_ex_atr": 0
                },
            request_only=True, 
            response_only=False,
        ),
    ]
)
class CDRefAsetExtAtrSerializers(serializers.ModelSerializer):

    nilai = serializers.CharField(max_length=100, default=None, allow_null=True)  
    status = serializers.IntegerField(default=1, allow_null=True)  
    
    id_ref_aset = serializers.SlugRelatedField(
        queryset=RefAset.objects.all(),
        slug_field='id_ref_aset',
        allow_null=False,
        style={'base_template': 'input.html'}
    ) 
    id_ref_aset_ex_atr = serializers.SlugRelatedField(
        queryset=RefAsetExAtr.objects.all(),
        slug_field='id_ref_aset_ex_atr',
        allow_null=False,
        required=True,
        style={'base_template': 'input.html'}
    ) 

    tgl_entri = serializers.DateField(format="%Y-%m-%d", read_only=True)
    tgl_update = serializers.DateField(format="%Y-%m-%d", read_only=TRUE) 

    class Meta:
        model = RefAsetExtAtr
        fields = '__all__' 

@extend_schema_serializer(
    exclude_fields=('id_ref_aset_ext_atr','tgl_entri','tgl_update'), # schema ignore these fields
    examples = [
         OpenApiExample(
            'Batch Example',
            summary='Batch Example',
            description='Batch Example',
            value=[
                {   
                    "id_ref_aset_ext_atr": 1,
                    "nilai": "string",
                    "status": 1,
                    "id_ref_aset": 0,
                    "id_ref_aset_ex_atr": 0 
                },
                {   
                    "id_ref_aset_ext_atr": 1,
                    "nilai": "string",
                    "status": 1,
                    "id_ref_aset": 0,
                    "id_ref_aset_ex_atr": 0
                }
            ],
            request_only=True, 
            response_only=False,
        )
    ]
)
class UDRefAsetExtAtrSerializers(serializers.ModelSerializer):
    queryset = RefAsetExtAtr.objects.all()

    nilai = serializers.CharField(max_length=100, required=False)  
    status = serializers.IntegerField(required=False)  
    
    id_ref_aset = serializers.SlugRelatedField(
        queryset=RefAset.objects.all(),
        slug_field='id_ref_aset',
        allow_null=False,
        required=False, 
        style={'base_template': 'input.html'}
    ) 
    id_ref_aset_ex_atr = serializers.SlugRelatedField(
        queryset=RefAsetExAtr.objects.all(),
        slug_field='id_ref_aset_ex_atr',
        allow_null=False,
        required=True,
        style={'base_template': 'input.html'}
    ) 

    class Meta:
        model = RefAsetExtAtr
        fields = '__all__'
