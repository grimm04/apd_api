from rest_framework import serializers

from .models import REF_PEGAWAI 
from datetime import datetime
from apps.users.models import Users
from apps.master.jaringan.ref_lokasi.models import RefLokasi

from apps.additional.serializers import UserDetailSerializerDef, IDSRef_LokasiSerializer



class REF_PEGAWAISerializers(serializers.ModelSerializer):  
    id_user = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    id_ref_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    tgl_entri = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None, required=False) 
    tgl_update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None, required=False) 

    user = UserDetailSerializerDef(read_only=True, source='id_user') 
    ref_lokasi = IDSRef_LokasiSerializer(read_only=True, source='id_ref_lokasi') 

    class Meta:
        model = REF_PEGAWAI
        fields = '__all__'



from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
@extend_schema_serializer(
    exclude_fields=[], # schema ignore these fields
    examples = [ 
         OpenApiExample(
            'Example',
            summary='Example',
            description='Example',
            value=
                {
                    "id_ref_pegawai": 0,
                    "id_user": 0,
                    "id_ref_lokasi": 0,
                    "tgl_entri": datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'),
                    "tgl_update": datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'),
                },
            request_only=True, 
            response_only=False,
        ),
    ]
)
class CDREF_PEGAWAISerializers(serializers.ModelSerializer):

    id_user = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    id_ref_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    tgl_entri = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None, required=False) 
    tgl_update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None, required=False) 

    user = UserDetailSerializerDef(read_only=True, source='id_user') 
    ref_lokasi = IDSRef_LokasiSerializer(read_only=True, source='id_ref_lokasi') 

    class Meta:
        model = REF_PEGAWAI
        fields = '__all__' 

@extend_schema_serializer(
    exclude_fields=[], # schema ignore these fields
    examples = [ 
         OpenApiExample(
            'Example',
            summary='Example',
            description='Example',
            value=
                {
                    "id_ref_pegawai": 0,
                    "id_user": 0,
                    "id_ref_lokasi": 0,
                    "tgl_entri": datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'),
                    "tgl_update": datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'),
                },
            request_only=True, 
            response_only=False,
        ),
    ]
)
class UDREF_PEGAWAISerializers(serializers.ModelSerializer):
    id_user = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    id_ref_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    tgl_entri = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None, required=False) 
    tgl_update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None, required=False) 

    user = UserDetailSerializerDef(read_only=True, source='id_user') 
    ref_lokasi = IDSRef_LokasiSerializer(read_only=True, source='id_ref_lokasi') 
    class Meta:
        model = REF_PEGAWAI
        fields = '__all__'

