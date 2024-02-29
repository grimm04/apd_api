from django.shortcuts import get_object_or_404

from rest_framework import generics, status, response, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from django_filters.rest_framework import DjangoFilterBackend

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import Roles
from . import serializers
from .filters import SearchFilter, RolesFilter

#custom pagination
from base.custom_pagination import CustomPagination
# base response  
from base.response import response__ ,get_response, post_update_response , not_found

class RolesViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = Roles.objects.all()
    serializer_class = serializers.CRRolesSerializers
    update_serializer_class = serializers.UDRolesSerializers  
    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = RolesFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['name', 'description']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id'] 

    @extend_schema(
        methods=["GET"],
        summary="Get Data Roles.",
        description="Get Data Roles.",
        parameters=[
            OpenApiParameter(name='page', description='page number, default: 1.', required=False, type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['admin']
    )
    def list(self, request): 
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'roles.view')   
    

    @extend_schema(
        methods=["POST"],
        summary="Create Data Roles.",
        description="Create Data Roles.",
        request=serializer_class,
        responses=serializer_class,
        tags=['admin']
    )
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer,'roles.create') 

        
    @extend_schema(
        methods=["GET"],
        summary="Display speciffied User",
        description="Get Details User",
        tags=['admin']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        roles = self.queryset.filter(id=pk)
        if roles is None :
            return not_found('roles.not_found')
        
        serializer = self.serializer_class(roles, many=True)
        return response__(request, serializer, 'roles.view') 

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Roles.",
        description="Update Data Roles.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['admin']
    )
    def update(self, request, pk):
        role = get_object_or_404(Roles, pk=pk) 
        serializer = self.update_serializer_class(instance=role, data=request.data) 

        return post_update_response(serializer, 'roles.update') 

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Roles.",
        description="Delete Data Roles.",
        request=serializer_class,
        responses=serializer_class,
        tags=['admin']
    )
    def destroy(self, request, pk):
        roles = get_object_or_404(Roles, pk=pk)
        self.perform_destroy(roles) 
        return response__(request, roles, 'roles.delete') 
    
    def perform_destroy(self, instance):
        instance.delete()
 