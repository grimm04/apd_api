from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.views import APIView 
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import TransPmJenisDoc
from .filters import TransPmJenisDocFilter, SearchFilter, TransPmJenisDoc

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination 

class TransPmJenisDocViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TransPmJenisDoc.objects.all()
    serializer_class = serializers.CRTransPmJenisDocSerializers
    update_serializer_class = serializers.UDTransPmJenisDocSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TransPmJenisDocFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['name']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_pm_jenis_doc']

    @extend_schema(
        methods=["GET"],
        summary="Get Trans Pm Jenis Doc",
        description="Get Trans Pm Jenis Doc",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['trans']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'trans_pm_jenis_doc.view')

    @extend_schema(
        methods=["POST"],
        summary="Create trans.",
        description="Create trans.",
        request=serializer_class,
        responses=serializer_class,
        tags=['trans']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'trans_pm_jenis_doc.create')

    @extend_schema(
        methods=["GET"],
        summary="Get trans (Specified).",
        description="Get trans (Specified).",
        tags=['trans']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        trans_pm_jenis_doc = self.queryset.filter(id_trans_pm_jenis_doc=pk)
        if not trans_pm_jenis_doc:
            return not_found('trans_pm_jenis_doc.not_found')

        serializer = self.serializer_class(trans_pm_jenis_doc, many=True)
        return response__(request, serializer, 'trans_pm_jenis_doc.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update trans",
        description="Update trans",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['trans']
    )
    def update(self, request, pk):
        trans_pm_jenis_doc = get_object_or_404(TransPmJenisDoc, pk=pk)
        serializer = self.update_serializer_class(instance=trans_pm_jenis_doc, data=request.data)

        return post_update_response(serializer, 'trans_pm_jenis_doc.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete trans.",
        description="Delete trans.",
        request=serializer_class,
        responses=serializer_class,
        tags=['trans']
    )
    def destroy(self, request, pk):
        trans_pm_jenis_doc = get_object_or_404(TransPmJenisDoc, pk=pk)
        self.perform_destroy(trans_pm_jenis_doc)
        return response__(request, trans_pm_jenis_doc, 'trans_pm_jenis_doc.delete')

    def perform_destroy(self, instance):
        instance.delete()
 