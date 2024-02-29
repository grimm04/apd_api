from rest_framework import serializers 
from apps.master.jaringan.ref_lokasi.models import RefLokasi 
from apps.additional.serializers import RefLokasiWParentSerializer, RefJenisLokasierializer
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample

class PenyulangUFRSerializer(serializers.ModelSerializer):  
    parent_lokasi = RefLokasiWParentSerializer(read_only=True, source='id_parent_lokasi')
    ref_jenis_lokasi = RefJenisLokasierializer(read_only=True, source='id_ref_jenis_lokasi')
    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi','id_parent_lokasi','id_ref_jenis_lokasi','nama_lokasi','kode_lokasi','ufr','parent_lokasi','ref_jenis_lokasi']


@extend_schema_serializer(
    exclude_fields=[],
    examples=[ 
        OpenApiExample(
            'Example',
            summary='Example',
            description='Example',
            value=
               {
                "id_ref_lokasi": [
                    1,2,3
                ],
                "ufr": 1
                },
            request_only=True,
            response_only=False,
        ),
    ]
)
class UpdatePenyulangUFRSerializer(serializers.ModelSerializer):   
    id_ref_lokasi  = serializers.ListField(child=serializers.CharField())
    ufr = serializers.IntegerField(allow_null=False, required=True)
    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi','ufr']
 