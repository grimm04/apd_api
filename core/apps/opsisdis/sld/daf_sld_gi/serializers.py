from rest_framework import serializers

from .models import DAF_SLD_GI 
from apps.master.jaringan.ref_lokasi.models import RefLokasi

from datetime import datetime


from apps.additional.serializers import IDSRef_LokasiSerializer



class DAF_SLD_GISerializers(serializers.ModelSerializer):
    nama_file = serializers.CharField(max_length=100) 
    kelompok = serializers.CharField(max_length=30, required=True) 
    keterangan = serializers.CharField(max_length=100,required=False)
    tgl_upload = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None, required=False) 
    id_gardu_induk = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    gardu_induk  = IDSRef_LokasiSerializer(read_only=True, source='id_gardu_induk') 

    class Meta:
        model = DAF_SLD_GI
        fields = '__all__'



from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
@extend_schema_serializer(
    exclude_fields=[], # schema ignore these fields
    examples = [
        #  OpenApiExample(
        #     'Batch Example',
        #     summary='Batch Example',
        #     description='Batch Example',
        #     value=[
        #         { 
        #             "id_wp_master_bagian": 1,
        #             "pekerjaan": "string",
        #             "lokasi_pekerjaan": "string",
        #             "tanggal": '2022-05-11 13:00'
        #         },
        #         { 
        #             "id_wp_master_bagian": 1,
        #             "pekerjaan": "string",
        #             "lokasi_pekerjaan": "string",
        #             "tanggal": '2022-05-11 13:00'
        #         },
                 
        #     ],
        #     request_only=True, 
        #     response_only=False,
        # ),
         OpenApiExample(
            'Example',
            summary='Example',
            description='Example',
            value=
                {  
                    "id_daf_sld_gi": 0,
                    "nama_file": "string",
                    "kelompok": "string",
                    "keterangan": "string",
                    "tgl_upload": datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'),
                    "id_gardu_induk": 0
                },
            request_only=True, 
            response_only=False,
        ),
    ]
)
class CDDAF_SLD_GISerializers(serializers.ModelSerializer):

    nama_file = serializers.CharField(max_length=100) 
    kelompok = serializers.CharField(max_length=30, required=True) 
    keterangan = serializers.CharField(max_length=100,required=False)
    tgl_upload = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None, required=False) 
    id_gardu_induk = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    # gardu_induk  = IDSRef_LokasiSerializer(read_only=True, source='id_gardu_induk') 

    class Meta:
        model = DAF_SLD_GI
        fields = '__all__' 

@extend_schema_serializer(
    exclude_fields=[], # schema ignore these fields
    examples = [
        #  OpenApiExample(
        #     'Batch Example',
        #     summary='Batch Example',
        #     description='Batch Example',
        #     value=[
        #         {   
        #             "id_DAF_SLD_GI":1,
        #             "id_wp_master_bagian": 1,
        #             "pekerjaan": "string",
        #             "lokasi_pekerjaan": "string",
        #             "tanggal": '2022-05-11 13:00'
        #         },
        #         { 
        #             "id_wp_master_bagian": 1,
        #             "pekerjaan": "string",
        #             "lokasi_pekerjaan": "string",
        #             "tanggal": '2022-05-11 13:00'
        #         },
        #     ],
        #     request_only=True, 
        #     response_only=False,
        # ),
         OpenApiExample(
            'Example',
            summary='Example',
            description='Example',
            value=
                 {  
                    "id_daf_sld_gi": 0,
                    "nama_file": "string",
                    "kelompok": "string",
                    "keterangan": "string",
                    "tgl_upload": datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'),
                    "id_gardu_induk": 0
                },
            request_only=True, 
            response_only=False,
        ),
    ]
)
class UDDAF_SLD_GISerializers(serializers.ModelSerializer):
    nama_file = serializers.CharField(max_length=100, required=False) 
    kelompok = serializers.CharField(max_length=30, required=True) 
    keterangan = serializers.CharField(max_length=100,required=False)
    tgl_upload = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None, required=False) 
    id_gardu_induk = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    gardu_induk  = IDSRef_LokasiSerializer(read_only=True, source='id_gardu_induk') 

    class Meta:
        model = DAF_SLD_GI
        fields = '__all__'

