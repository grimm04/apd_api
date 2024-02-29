from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import TransJadwalHarGardu
from .filters import TransJadwalHarGarduFilter, SearchFilter, TransJadwalHarGardu

from base.response import response__, get_response, post_update_response, not_found,response_basic,res_serializer_error
from base.custom_pagination import CustomPagination 

class TransJadwalHarGarduViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TransJadwalHarGardu.objects.all()
    serializer_class = serializers.TransJadwalHarGarduSerializers
    create_serializer_class = serializers.CRTransJadwalHarGarduSerializers
    create_save_serializer_class = serializers.CreateSaveTransJadwalHarGarduSerializers
    update_serializer_class = serializers.UDTransJadwalHarGarduSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TransJadwalHarGarduFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = []  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_jadwal_har_gardu']

    @extend_schema(
        methods=["GET"],
        summary="Get Opsisdis - Jadwal Pemeliharaan - Har Gardu.",
        description="Get Opsisdis - Jadwal Pemeliharaan - Har Gardu.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'trans_jadwal_har_gardu.view')


    @extend_schema(
        methods=["POST"],
        summary="Create Opsisdis - Jadwal Pemeliharaan - Har Gardu.",
        description="Create Opsisdis - Jadwal Pemeliharaan - Har Gardu.",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    # create
    def create(self, request):
        data = request.data  
        serializer = self.create_serializer_class(data=data)
        if serializer.is_valid(): 
            id_gardu = data['id_gardu']
            id_trans_jadwal_har = data['id_trans_jadwal_har'] 
            data = list()
            for gi in id_gardu: 
                d = {
                  'id_gardu':  gi,
                  'id_trans_jadwal_har':id_trans_jadwal_har
                }
                data.append(d)   
            serializer = self.create_save_serializer_class(data=data, many=True) 
            return post_update_response(serializer, 'trans_jadwal_har_gardu.create')  
        return res_serializer_error(serializer=serializer)  

    @extend_schema(
        methods=["GET"],
        summary="Get Opsisdis - Jadwal Pemeliharaan - Har Gardu (Specified).",
        description="Get Opsisdis - Jadwal Pemeliharaan - Har Gardu (Specified).",
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        trans_jadwal_har = self.queryset.filter(id_trans_jadwal_har=pk)
        if not trans_jadwal_har:
            return not_found('trans_jadwal_har_gardu.not_found')

        serializer = self.serializer_class(trans_jadwal_har, many=True)
        return response__(request, serializer, 'trans_jadwal_har_gardu.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Opsisdis - Jadwal Pemeliharaan - Har Gardu.",
        description="Update Opsisdis - Jadwal Pemeliharaan - Har Gardu.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def update(self, request, pk):
        trans_jadwal_har = get_object_or_404(TransJadwalHarGardu, pk=pk)
        serializer = self.update_serializer_class(instance=trans_jadwal_har, data=request.data)

        return post_update_response(serializer, 'trans_jadwal_har_gardu.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Opsisdis - Jadwal Pemeliharaan - Har Gardu.",
        description="Delete Opsisdis - Jadwal Pemeliharaan - Har Gardu.",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def destroy(self, request, pk):
        trans_jadwal_har = get_object_or_404(TransJadwalHarGardu, pk=pk)
        self.perform_destroy(trans_jadwal_har)
        return response__(request, trans_jadwal_har, 'trans_jadwal_har_gardu.delete')

    def perform_destroy(self, instance):
        instance.delete()