from rest_framework import serializers
from .models import TelemetringPenyulang
from apps.master.jaringan.ref_lokasi.models import RefLokasi
from apps.users.models import Users
from datetime import datetime
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from apps.additional.serializers import IDSRef_LokasiADDSerializer 



class SubRefParentLokasiSerializer(serializers.ModelSerializer):

    nama_parent_lokasi = serializers.CharField(source='nama_lokasi')
    
    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi','nama_lokasi', 'nama_parent_lokasi', 'kode_lokasi', 'id_parent_lokasi','no_urut']

class SubRefParentLokasiGISerializer(serializers.ModelSerializer):
    parent_lokasi = SubRefParentLokasiSerializer(read_only=True, source='id_parent_lokasi') 
    nama_parent_lokasi = serializers.CharField(source='nama_lokasi')  
    nama_gardu_induk = serializers.SerializerMethodField()  
    class Meta:
        model = RefLokasi 
        fields = ['id_ref_lokasi','nama_lokasi', 'nama_parent_lokasi','kode_lokasi', 'nama_gardu_induk','id_parent_lokasi','no_urut','parent_lokasi','jenis_layanan','sinkron_data','def_pengukuran_teg_primer','def_pengukuran_teg_sekunder','def_nilai_cosq']

    def get_nama_gardu_induk(self,obj):
        return obj.id_parent_lokasi.nama_lokasi
class GetTelemetringPenyulangSerializers(serializers.ModelSerializer): 
    # ref_lokasi = SubRefParentLokasiGISerializer(read_only=True, source='id_lokasi') 
    class Meta:
        model = TelemetringPenyulang
        fields = '__all__'

class SubUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['fullname', 'nip', 'gender']

@extend_schema_serializer(
    exclude_fields=('id_trans_tm_penyulang', 'tgl_entri', 'tgl_update'),
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
class TelemetringPenyulangSerializers(serializers.ModelSerializer):
    datum = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    i = serializers.DecimalField(allow_null=True,max_digits=5, decimal_places=2,required=False)
    v = serializers.DecimalField(allow_null=True,max_digits=5, decimal_places=2,required=False)
    p = serializers.DecimalField(allow_null=True,max_digits=5, decimal_places=2,required=False)
    q = serializers.DecimalField(allow_null=True,max_digits=5, decimal_places=2,required=False)
    f = serializers.DecimalField(allow_null=True,max_digits=5, decimal_places=2,required=False)  
    cosq = serializers.DecimalField(allow_null=True, max_digits=5, decimal_places=2,required=False)
    no_urut_cell = serializers.IntegerField(allow_null=True, required=False)
    id_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_lokasi = IDSRef_LokasiADDSerializer(read_only=True, source='id_lokasi')
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
    user_entri = SubUsersSerializer(read_only=True, source='id_user_entri')
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    user_update = SubUsersSerializer(read_only=True, source='id_user_update')
    date_hari = serializers.DateTimeField(read_only=True, source='datum', format="%Y-%m-%d")
    jam = serializers.DateTimeField(read_only=True, source='datum', format="%H:%M:%S")
    class Meta:
        model = TelemetringPenyulang
        fields = '__all__'

@extend_schema_serializer(
    exclude_fields=('id_trans_tm_penyulang', 'tgl_entri', 'tgl_update'),
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
                    "id_trans_tm_penyulang": 1,
                    "id_user_update": 1
                },
                {
                    "i": 6,
                    "v": 7,
                    "p": 8,
                    "q": 9,
                    "f": 10,
                    "id_trans_tm_penyulang": 2,
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
                    "id_trans_tm_penyulang": 1,
                    "id_user_update": 1
                },
            request_only=True,
            response_only=False,
        ),
    ]
)
class UDTelemetringPenyulangSerializers(serializers.ModelSerializer):
    i = serializers.DecimalField(allow_null=True,max_digits=5, decimal_places=2,required=False)
    v = serializers.DecimalField(allow_null=True,max_digits=5, decimal_places=2,required=False)
    p = serializers.DecimalField(allow_null=True,max_digits=5, decimal_places=2,required=False)
    q = serializers.DecimalField(allow_null=True,max_digits=5, decimal_places=2,required=False)
    f = serializers.DecimalField(allow_null=True,max_digits=5, decimal_places=2,required=False)  
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

    class Meta:
        model = TelemetringPenyulang
        fields = '__all__'

@extend_schema_serializer(
    exclude_fields=('id_trans_tm_penyulang', 'tgl_entri', 'tgl_update'),
    examples=[
         OpenApiExample(
            'Single Example',
            summary='Single Example',
            description='Single Example',
            value=
                {
                    "id_user_entri": 1,
                    "id_gardu_induk": 1,
                    "id_parent_lokasi": 1,
                    "id_lokasi": 1,
                    "datum": datetime.today().strftime('%Y-%m-%d')
                },
            request_only=True,
            response_only=False,
        ),
    ]
)
class TelemetringPenyulangGenerateSerializers(serializers.Serializer):
    # id_parent_lokasi = serializers.SlugRelatedField(
    #     queryset=RefLokasi.objects.all(),
    #     slug_field='id_ref_lokasi',
    #     allow_null=True,
    #     required=True,
    #     style={'base_template': 'input.html'}
    # )
    id_gardu_induk = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=False,
        style={'base_template': 'input.html'} 
    )

    id_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
   
    # datum = serializers.DateTimeField(format="%Y-%m-%d",required=True)
 