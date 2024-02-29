from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import RefJenisPekerjaan
from .filters import RefJenisPekerjaanFilter, SearchFilter, RefJenisPekerjaan

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination 

class RefJenisPekerjaanViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefJenisPekerjaan.objects.all()
    serializer_class = serializers.RefJenisPekerjaanSerializers 

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = RefJenisPekerjaanFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['name']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_ref_jenis_pekerjaan']

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Opsisdis - Ref Jenis Pekerjaan.",
        description="Get Master Data - Opsisdis - Ref Jenis Pekerjaan.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_opsisdis']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'ref_jenis_pekerjaan.view')


    @extend_schema(
        methods=["POST"],
        summary="Create Master Data - Opsisdis - Ref Jenis Pekerjaan.",
        description="Create Master Data - Opsisdis - Ref Jenis Pekerjaan.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_opsisdis']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'ref_jenis_pekerjaan.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Opsisdis - Ref Jenis Pekerjaan (Specified).",
        description="Get Master Data - Opsisdis - Ref Jenis Pekerjaan (Specified).",
        tags=['master_opsisdis']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ref_jenis_pekerjaan = self.queryset.filter(id_ref_jenis_pekerjaan=pk)
        if not ref_jenis_pekerjaan:
            return not_found('ref_jenis_pekerjaan.not_found')

        serializer = self.serializer_class(ref_jenis_pekerjaan, many=True)
        return response__(request, serializer, 'ref_jenis_pekerjaan.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Master Data - Opsisdis -  Ref Jenis Pekerjaan.",
        description="Update Master Data - Opsisdis -  Ref Jenis Pekerjaan.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_opsisdis']
    )
    def update(self, request, pk):
        ref_jenis_pekerjaan = get_object_or_404(RefJenisPekerjaan, pk=pk)
        serializer = self.serializer_class(instance=ref_jenis_pekerjaan, data=request.data)

        return post_update_response(serializer, 'ref_jenis_pekerjaan.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Master Data - Opsisdis - Ref Jenis Pekerjaan.",
        description="Delete Master Data - Opsisdis - Ref Jenis Pekerjaan.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_opsisdis']
    )
    def destroy(self, request, pk):
        ref_jenis_pekerjaan = get_object_or_404(RefJenisPekerjaan, pk=pk)
        self.perform_destroy(ref_jenis_pekerjaan)
        return response__(request, ref_jenis_pekerjaan, 'ref_jenis_pekerjaan.delete')

    def perform_destroy(self, instance):
        instance.delete()