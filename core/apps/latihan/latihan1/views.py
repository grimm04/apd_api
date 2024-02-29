from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .models import LATIHAN 
from . import serializers
from .filters import SearchFilter, LATIHANFilter
from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination



class Latihan1Views(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = LATIHAN.objects.all()
    serializer_class = serializers.LATIHANSerializers
    # create_serializer_class = serializers.CRLATIHANCSerializers
    # update_serializer_class = serializers.UDLATIHANSerializers

    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_class = LATIHANFilter
    filterset_fields = ['keyword']
    search_fields = ['nama']
    ordering_fields = '__all__'
    ordering = ['id_latihan']

    @extend_schema(
        methods=["GET"],
        summary="Get His Latihan",
        description="Get His Latihan",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=15), 
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['latihan']
    )
    def list(self, request): 

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'latihan.view')  

    @extend_schema(
        methods=["POST"],
        summary="Create His Latihan",
        description="Create His Latihan",
        request=serializer_class,
        responses=serializer_class,
        tags=['latihan']
    )
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'latihan.create')

    @extend_schema(
        methods=["GET"],
        summary="Display speciffied Histori Latihan",
        description="Get Details Histori Latihan",
        tags=['latihan']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        latihan = self.queryset.filter(pk=pk)
        if not latihan:
            return not_found('latihan.not_found')

        serializer = self.serializer_class(latihan, many=True)
        return response__(request, serializer, 'latihan.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update His Latihan",
        description="Update His Latihan",
        request=serializer_class,
        responses=serializer_class,
        tags=['latihan']
    )
    def update(self, request, pk):
        latihan = get_object_or_404(LATIHAN, pk=pk)
        serializer = self.serializer_class(instance=latihan, data=request.data)

        return post_update_response(serializer, 'latihan.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delett His Latihan",
        description="Delett His Latihan",
        request=serializer_class,
        responses=serializer_class,
        tags=['latihan']
    )
    def destroy(self, request, pk):
        latihan = get_object_or_404(LATIHAN, pk=pk)
        self.perform_destroy(latihan)
        return response__(request, latihan, 'latihan.delete')

    def perform_destroy(self, instance):
        instance.delete()

