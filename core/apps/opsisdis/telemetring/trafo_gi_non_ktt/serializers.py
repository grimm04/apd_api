from rest_framework import serializers
from .models import TelemetringTrafoGI
from apps.master.jaringan.ref_lokasi.models import RefLokasi
from apps.users.models import Users
from datetime import datetime
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from apps.additional.serializers import IDSRef_LokasiSerializer,SubRefParentLokasiGISerializer 
  

class SubUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['fullname', 'nip', 'gender']

class GetTelemetringTrafoGISerializers(serializers.ModelSerializer): 
    ref_lokasi = SubRefParentLokasiGISerializer(read_only=True, source='id_lokasi')

    class Meta:
        model = TelemetringTrafoGI
        fields = '__all__'

@extend_schema_serializer(
    exclude_fields=('id_trans_tm_trafo_gi', 'tgl_entri', 'tgl_update'),
    examples=[
         OpenApiExample(
            'Batch Example',
            summary='Batch Example',
            description='Batch Example',
            value=[
                {
                    "datum": datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'),
                    "i": 1,
                    "v": 2,
                    "p": 3,
                    "q": 4,
                    "f": 5,
                    "cosq": 0.95,
                    "id_lokasi": 112,
                    "id_parent_lokasi": 1,
                    "id_user_entri": 1,
                    "id_user_update": 1
                },
                {
                    "datum": datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'),
                    "i": 6,
                    "v": 7,
                    "p": 8,
                    "q": 9,
                    "f": 10,
                    "cosq": 0.95,
                    "id_lokasi": 113,
                    "id_parent_lokasi": 1,
                    "id_user_entri": 13,
                    "id_user_update": 13
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
                    "datum": datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'),
                    "i": 1,
                    "v": 2,
                    "p": 3,
                    "q": 4,
                    "f": 5,
                    "cosq": 0.95,
                    "id_lokasi": 112,
                    "id_parent_lokasi": 1,
                    "id_user_entri": 1,
                    "id_user_update": 1
                },
            request_only=True,
            response_only=False,
        ),
    ]
)
class TelemetringTrafoGISerializers(serializers.ModelSerializer):
    datum = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    i = serializers.DecimalField(allow_null=True, max_digits=5, decimal_places=2,required=False)
    v = serializers.DecimalField(allow_null=True, max_digits=5, decimal_places=2,required=False)
    p = serializers.DecimalField(allow_null=True, max_digits=5, decimal_places=2,required=False)
    q = serializers.DecimalField(allow_null=True, max_digits=5, decimal_places=2,required=False)
    f = serializers.DecimalField(allow_null=True, max_digits=5, decimal_places=2,required=False)
    cosq = serializers.DecimalField(allow_null=True, max_digits=5, decimal_places=2,required=False)
    no_urut_cell = serializers.IntegerField(allow_null=True, required=False) 
    id_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_lokasi = IDSRef_LokasiSerializer(read_only=True, source='id_lokasi')
    id_parent_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_parent_lokasi = SubRefParentLokasiGISerializer(read_only=True, source='id_parent_lokasi')
    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 
    sinkron_data = serializers.CharField(max_length=30, allow_null=True,allow_blank=True, required=False) 
    id_ref_lokasi_area = serializers.IntegerField(default=None, allow_null=True,required=False)
    date_hari = serializers.DateTimeField(read_only=True, source='datum', format="%Y-%m-%d")
    jam = serializers.DateTimeField(read_only=True, source='datum', format="%H:%M:%S")
    class Meta:
        model = TelemetringTrafoGI
        fields = '__all__'

@extend_schema_serializer(
    exclude_fields=('id_trans_tm_trafo_gi', 'tgl_entri', 'tgl_update'),
    examples=[
         OpenApiExample(
            'Batch Example',
            summary='Batch Example',
            description='Batch Example',
            value=[
                {
                    "i": 1,
                    "v": 2,
                    "p": 3,
                    "q": 4,
                    "f": 5,
                    "cosq": 0.95,
                    "id_trans_tm_trafo_gi": 1,
                    "id_user_update": 1
                },
                {
                    "i": 6,
                    "v": 7,
                    "p": 8,
                    "q": 9,
                    "f": 10,
                    "cosq": 0.95,
                    "id_trans_tm_trafo_gi": 2,
                    "id_user_update": 5
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
                    "i": 1,
                    "v": 2,
                    "p": 3,
                    "q": 4,
                    "f": 5,
                    "cosq": 0.95,
                    "id_trans_tm_trafo_gi": 1,
                    "id_user_update": 1
                },
            request_only=True,
            response_only=False,
        ),
    ]
)
class UDTelemetringTrafoGISerializers(serializers.ModelSerializer): 
    i = serializers.DecimalField(allow_null=True, max_digits=5, decimal_places=2 , required=False)
    v = serializers.DecimalField(allow_null=True, max_digits=5, decimal_places=2 , required=False)
    p = serializers.DecimalField(allow_null=True, max_digits=5, decimal_places=2 , required=False)
    q = serializers.DecimalField(allow_null=True, max_digits=5, decimal_places=2 , required=False)
    f = serializers.DecimalField(allow_null=True, max_digits=5, decimal_places=2 , required=False)
    cosq = serializers.DecimalField(allow_null=True, max_digits=5, decimal_places=2,required=False) 
    no_urut_cell = serializers.IntegerField(allow_null=True, required=False) 
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    # user_update = SubUsersSerializer(read_only=True, source='id_user_update')
    sinkron_data = serializers.CharField(max_length=30, allow_null=True,allow_blank=True, required=False) 
    id_ref_lokasi_area = serializers.IntegerField(allow_null=True,required=False)
    class Meta:
        model = TelemetringTrafoGI
        fields = '__all__'

@extend_schema_serializer(
    exclude_fields=('id_trans_tm_trafo_gi', 'tgl_entri', 'tgl_update'),
    examples=[
         OpenApiExample(
            'Single Example',
            summary='Single Example',
            description='Single Example',
            value=
                {
                    "id_user_entri": 1,
                    "id_parent_lokasi": 1,
                    "id_lokasi": 1,
                    "datum": datetime.today().strftime('%Y-%m-%d')
                },
            request_only=True,
            response_only=False,
        ),
    ]
)
class TelemetringTrafoGIGenerateSerializers(serializers.Serializer):
    id_parent_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'} 
    )

    id_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    # datum = serializers.DateTimeField(required=True)

    # class Meta:
    #     model = TelemetringTrafoGI
    #     fields = '__all__'