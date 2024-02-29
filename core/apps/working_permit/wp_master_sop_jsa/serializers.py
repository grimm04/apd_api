from rest_framework import serializers

from .models import WP_MASTER_SOP_JSA 
from apps.master.working_permit.wm_bagian.models import WP_BAGIAN

from apps.additional.serializers import WP_BAGIANSerializer

 

class WP_MASTER_SOP_JSASerializers(serializers.ModelSerializer):
    judul_pekerjaan = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    nomor = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    nama_file = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah1 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah2 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah3 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah4 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah5 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah6 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah7 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah8 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah9 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah10 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah11 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah12 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah13 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah14 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah15 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi1 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi2 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi3 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi4 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi5 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi6 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi7 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi8 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi9 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi10 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi11 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi12 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi13 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi14 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi15 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    pengendalian1 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian2 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian3 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian4 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian5 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian6 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian7 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian8 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian9 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian10 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian11 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian12 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian13 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian14 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian15 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)  

    tgl_entri = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None) 
    tgl_update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None) 
    id_wp_master_bagian = serializers.SlugRelatedField(
        queryset=WP_BAGIAN.objects.all(),
        slug_field='id_wp_master_bagian',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    bagian = WP_BAGIANSerializer(read_only=True, source='id_wp_master_bagian') 

    class Meta:
        model = WP_MASTER_SOP_JSA
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
                    "judul_pekerjaan": "string",
                    "nomor": "string",
                    "nama_file": "string",
                    "langkah1": "string",
                    "langkah2": "string",
                    "langkah3": "string",
                    "langkah4": "string",
                    "langkah5": "string",
                    "langkah6": "string",
                    "langkah7": "string",
                    "langkah8": "string",
                    "langkah9": "string",
                    "langkah10": "string",
                    "langkah11": "string",
                    "langkah12": "string",
                    "langkah13": "string",
                    "langkah14": "string",
                    "langkah15": "string",
                    "potensi1": "string",
                    "potensi2": "string",
                    "potensi3": "string",
                    "potensi4": "string",
                    "potensi5": "string",
                    "potensi6": "string",
                    "potensi7": "string",
                    "potensi8": "string",
                    "potensi9": "string",
                    "potensi10": "string",
                    "potensi11": "string",
                    "potensi12": "string",
                    "potensi13": "string",
                    "potensi14": "string",
                    "potensi15": "string",
                    "pengendalian1": "string",
                    "pengendalian2": "string",
                    "pengendalian3": "string",
                    "pengendalian4": "string",
                    "pengendalian5": "string",
                    "pengendalian6": "string",
                    "pengendalian7": "string",
                    "pengendalian8": "string",
                    "pengendalian9": "string",
                    "pengendalian10": "string",
                    "pengendalian11": "string",
                    "pengendalian12": "string",
                    "pengendalian13": "string",
                    "pengendalian14": "string",
                    "pengendalian15": "string",
                    "tgl_entri": "2021-09-07 00:00:00",
                    "tgl_update": "2021-09-07 00:00:00",
                    "id_wp_master_bagian": 1
                },
                { 
                    "judul_pekerjaan": "string",
                    "nomor": "string",
                    "nama_file": "string",
                    "langkah1": "string",
                    "langkah2": "string",
                    "langkah3": "string",
                    "langkah4": "string",
                    "langkah5": "string",
                    "langkah6": "string",
                    "langkah7": "string",
                    "langkah8": "string",
                    "langkah9": "string",
                    "langkah10": "string",
                    "langkah11": "string",
                    "langkah12": "string",
                    "langkah13": "string",
                    "langkah14": "string",
                    "langkah15": "string",
                    "potensi1": "string",
                    "potensi2": "string",
                    "potensi3": "string",
                    "potensi4": "string",
                    "potensi5": "string",
                    "potensi6": "string",
                    "potensi7": "string",
                    "potensi8": "string",
                    "potensi9": "string",
                    "potensi10": "string",
                    "potensi11": "string",
                    "potensi12": "string",
                    "potensi13": "string",
                    "potensi14": "string",
                    "potensi15": "string",
                    "pengendalian1": "string",
                    "pengendalian2": "string",
                    "pengendalian3": "string",
                    "pengendalian4": "string",
                    "pengendalian5": "string",
                    "pengendalian6": "string",
                    "pengendalian7": "string",
                    "pengendalian8": "string",
                    "pengendalian9": "string",
                    "pengendalian10": "string",
                    "pengendalian11": "string",
                    "pengendalian12": "string",
                    "pengendalian13": "string",
                    "pengendalian14": "string",
                    "pengendalian15": "string",
                    "tgl_entri": "2021-09-07 00:00:00",
                    "tgl_update": "2021-09-07 00:00:00",
                    "id_wp_master_bagian": 1
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
                    "judul_pekerjaan": "string",
                    "nomor": "string",
                    "nama_file": "string",
                    "langkah1": "string",
                    "langkah2": "string",
                    "langkah3": "string",
                    "langkah4": "string",
                    "langkah5": "string",
                    "langkah6": "string",
                    "langkah7": "string",
                    "langkah8": "string",
                    "langkah9": "string",
                    "langkah10": "string",
                    "langkah11": "string",
                    "langkah12": "string",
                    "langkah13": "string",
                    "langkah14": "string",
                    "langkah15": "string",
                    "potensi1": "string",
                    "potensi2": "string",
                    "potensi3": "string",
                    "potensi4": "string",
                    "potensi5": "string",
                    "potensi6": "string",
                    "potensi7": "string",
                    "potensi8": "string",
                    "potensi9": "string",
                    "potensi10": "string",
                    "potensi11": "string",
                    "potensi12": "string",
                    "potensi13": "string",
                    "potensi14": "string",
                    "potensi15": "string",
                    "pengendalian1": "string",
                    "pengendalian2": "string",
                    "pengendalian3": "string",
                    "pengendalian4": "string",
                    "pengendalian5": "string",
                    "pengendalian6": "string",
                    "pengendalian7": "string",
                    "pengendalian8": "string",
                    "pengendalian9": "string",
                    "pengendalian10": "string",
                    "pengendalian11": "string",
                    "pengendalian12": "string",
                    "pengendalian13": "string",
                    "pengendalian14": "string",
                    "pengendalian15": "string",
                    "tgl_entri": "2021-09-07 00:00:00",
                    "tgl_update": "2021-09-07 00:00:00",
                    "id_wp_master_bagian": 1
                    },
            request_only=True, 
            response_only=False,
        ),
    ]
)
class CDWP_MASTER_SOP_JSASerializers(serializers.ModelSerializer): 
    judul_pekerjaan = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    nomor = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    nama_file = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah1 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah2 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah3 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah4 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah5 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah6 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah7 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah8 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah9 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah10 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah11 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah12 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah13 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah14 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah15 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi1 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi2 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi3 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi4 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi5 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi6 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi7 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi8 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi9 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi10 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi11 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi12 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi13 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi14 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi15 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    pengendalian1 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian2 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian3 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian4 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian5 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian6 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian7 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian8 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian9 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian10 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian11 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian12 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian13 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian14 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian15 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)  

    tgl_entri = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None) 
    tgl_update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None) 
    id_wp_master_bagian = serializers.SlugRelatedField(
        queryset=WP_BAGIAN.objects.all(),
        slug_field='id_wp_master_bagian',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )

    class Meta:
        model = WP_MASTER_SOP_JSA
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
                    "id_wp_master_sop_jasa": 0,
                    "judul_pekerjaan": "string",
                    "nomor": "string",
                    "nama_file": "string",
                    "langkah1": "string",
                    "langkah2": "string",
                    "langkah3": "string",
                    "langkah4": "string",
                    "langkah5": "string",
                    "langkah6": "string",
                    "langkah7": "string",
                    "langkah8": "string",
                    "langkah9": "string",
                    "langkah10": "string",
                    "langkah11": "string",
                    "langkah12": "string",
                    "langkah13": "string",
                    "langkah14": "string",
                    "langkah15": "string",
                    "potensi1": "string",
                    "potensi2": "string",
                    "potensi3": "string",
                    "potensi4": "string",
                    "potensi5": "string",
                    "potensi6": "string",
                    "potensi7": "string",
                    "potensi8": "string",
                    "potensi9": "string",
                    "potensi10": "string",
                    "potensi11": "string",
                    "potensi12": "string",
                    "potensi13": "string",
                    "potensi14": "string",
                    "potensi15": "string",
                    "pengendalian1": "string",
                    "pengendalian2": "string",
                    "pengendalian3": "string",
                    "pengendalian4": "string",
                    "pengendalian5": "string",
                    "pengendalian6": "string",
                    "pengendalian7": "string",
                    "pengendalian8": "string",
                    "pengendalian9": "string",
                    "pengendalian10": "string",
                    "pengendalian11": "string",
                    "pengendalian12": "string",
                    "pengendalian13": "string",
                    "pengendalian14": "string",
                    "pengendalian15": "string",
                    "tgl_entri": "2021-09-07 00:00:00",
                    "tgl_update": "2021-09-07 00:00:00",
                    "id_wp_master_bagian": 1
                },
                {
                    "id_wp_master_sop_jasa": 0,
                    "judul_pekerjaan": "string",
                    "nomor": "string",
                    "nama_file": "string",
                    "langkah1": "string",
                    "langkah2": "string",
                    "langkah3": "string",
                    "langkah4": "string",
                    "langkah5": "string",
                    "langkah6": "string",
                    "langkah7": "string",
                    "langkah8": "string",
                    "langkah9": "string",
                    "langkah10": "string",
                    "langkah11": "string",
                    "langkah12": "string",
                    "langkah13": "string",
                    "langkah14": "string",
                    "langkah15": "string",
                    "potensi1": "string",
                    "potensi2": "string",
                    "potensi3": "string",
                    "potensi4": "string",
                    "potensi5": "string",
                    "potensi6": "string",
                    "potensi7": "string",
                    "potensi8": "string",
                    "potensi9": "string",
                    "potensi10": "string",
                    "potensi11": "string",
                    "potensi12": "string",
                    "potensi13": "string",
                    "potensi14": "string",
                    "potensi15": "string",
                    "pengendalian1": "string",
                    "pengendalian2": "string",
                    "pengendalian3": "string",
                    "pengendalian4": "string",
                    "pengendalian5": "string",
                    "pengendalian6": "string",
                    "pengendalian7": "string",
                    "pengendalian8": "string",
                    "pengendalian9": "string",
                    "pengendalian10": "string",
                    "pengendalian11": "string",
                    "pengendalian12": "string",
                    "pengendalian13": "string",
                    "pengendalian14": "string",
                    "pengendalian15": "string",
                    "tgl_entri": "2021-09-07 00:00:00",
                    "tgl_update": "2021-09-07 00:00:00",
                    "id_wp_master_bagian": 1
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
                    "id_wp_master_sop_jasa": 0,
                    "judul_pekerjaan": "string",
                    "nomor": "string",
                    "nama_file": "string",
                    "langkah1": "string",
                    "langkah2": "string",
                    "langkah3": "string",
                    "langkah4": "string",
                    "langkah5": "string",
                    "langkah6": "string",
                    "langkah7": "string",
                    "langkah8": "string",
                    "langkah9": "string",
                    "langkah10": "string",
                    "langkah11": "string",
                    "langkah12": "string",
                    "langkah13": "string",
                    "langkah14": "string",
                    "langkah15": "string",
                    "potensi1": "string",
                    "potensi2": "string",
                    "potensi3": "string",
                    "potensi4": "string",
                    "potensi5": "string",
                    "potensi6": "string",
                    "potensi7": "string",
                    "potensi8": "string",
                    "potensi9": "string",
                    "potensi10": "string",
                    "potensi11": "string",
                    "potensi12": "string",
                    "potensi13": "string",
                    "potensi14": "string",
                    "potensi15": "string",
                    "pengendalian1": "string",
                    "pengendalian2": "string",
                    "pengendalian3": "string",
                    "pengendalian4": "string",
                    "pengendalian5": "string",
                    "pengendalian6": "string",
                    "pengendalian7": "string",
                    "pengendalian8": "string",
                    "pengendalian9": "string",
                    "pengendalian10": "string",
                    "pengendalian11": "string",
                    "pengendalian12": "string",
                    "pengendalian13": "string",
                    "pengendalian14": "string",
                    "pengendalian15": "string",
                    "tgl_entri": "2021-09-07 00:00:00",
                    "tgl_update": "2021-09-07 00:00:00",
                    "id_wp_master_bagian": 1
                },
            request_only=True, 
            response_only=False,
        ),
    ]
)
class UDWP_MASTER_SOP_JSASerializers(serializers.ModelSerializer):
    judul_pekerjaan = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    nomor = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    nama_file = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah1 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah2 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah3 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah4 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah5 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah6 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah7 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah8 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah9 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah10 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah11 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah12 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah13 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah14 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    langkah15 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi1 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi2 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi3 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi4 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi5 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi6 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi7 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi8 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi9 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi10 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi11 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi12 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi13 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi14 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    potensi15 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True) 
    pengendalian1 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian2 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian3 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian4 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian5 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian6 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian7 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian8 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian9 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian10 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian11 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian12 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian13 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian14 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)   
    pengendalian15 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)  

    tgl_entri = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None) 
    tgl_update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None) 
    id_wp_master_bagian = serializers.SlugRelatedField(
        queryset=WP_BAGIAN.objects.all(),
        slug_field='id_wp_master_bagian',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )

    class Meta:
        model = WP_MASTER_SOP_JSA
        fields = '__all__'

