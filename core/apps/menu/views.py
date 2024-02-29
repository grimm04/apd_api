import json
import re
from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from django_filters.rest_framework import DjangoFilterBackend

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import Menu
from . import serializers
from .filters import SearchFilter, MenuFilter

# base response 
from base.response import response__, get_response, post_update_response, not_found, response_basic

# custom pagination
from base.custom_pagination import CustomPagination


class MenuViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = Menu.objects.all()
    serializer_class = serializers.CRMenuSerializers
    update_serializer_class = serializers.UDMenuSerializers
    update_batch_serializer_class = serializers.UDBatchMenuSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = MenuFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['display', 'name', 'path']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Menu.",
        description="Get Data Menu.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['admin']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'menu.view')

    def validate_no(self, no):
        try:
            return int(no)
        except ValueError:
            return 0

    @extend_schema(
        methods=["POST"],
        summary="Create Data Menu.",
        description="Create Data Menu.",
        request=serializer_class,
        responses=serializer_class,
        tags=['admin']
    )
    # create
    def create(self, request):
        data = request.data
        if 'no' in data:
            no = data.get('no')
            data['no'] = self.validate_no(no)

        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'menu.create')

    @extend_schema(
        methods=["GET"],
        summary="Display speciffied User",
        description="Get Details User",
        tags=['admin']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        menu = self.queryset.filter(id=pk)
        if menu is None:
            return not_found('menu.not_found')

        serializer = self.serializer_class(menu, many=True)
        return response__(request, serializer, 'menu.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Menu.",
        description="Update Data Menu.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['admin']
    )
    def update(self, request, pk):
        menu = get_object_or_404(Menu, pk=pk)
        serializer = self.update_serializer_class(instance=menu, data=request.data)

        return post_update_response(serializer, 'menu.update')

    # update batch
    def get_data(self, obj_id):
        try:
            data_menu = Menu.objects.get(id=obj_id)
            return True, data_menu
        except Exception as e:
            return False, e

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Menu Batch.",
        description="Update Data Menu Batch, Can Be Multiple Update.",
        request=update_batch_serializer_class,
        responses=update_serializer_class,
        tags=['admin']
    )
    @action(detail=False, methods=['PUT'], url_path='update_menu_batch', url_name='update_menu_batch')
    def batch(self, request):
        update_data = request.data
        is_many = isinstance(update_data, list)
        if is_many:
            instances = []
            for data in update_data:
                id_menu = data['id']
                no = data['no']

                _, obj = self.get_data(id_menu)
                if _:
                    obj.no = no
                    obj.save()
                    instances.append(self.serializer_class(instance=obj).data)

            if instances:
                return response_basic(_status=True, results=instances, msg='menu.update')
            else:
                return response_basic(msg='menu.update_failed')
        else:
            id_menu = update_data['id']
            no = update_data['no']

            _, obj = self.get_data(id_menu)
            if _:
                obj.no = no
                obj.save()

                return response_basic(_status=True, results=self.serializer_class(instance=obj).data, msg='menu.update')
            else:
                return response_basic(msg='menu.update_failed')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Menu.",
        description="Delete Data Menu.",
        request=serializer_class,
        responses=serializer_class,
        tags=['admin']
    )
    def destroy(self, request, pk):
        menu = get_object_or_404(Menu, pk=pk)
        self.perform_destroy(menu)
        return response__(request, menu, 'menu.delete')

    def perform_destroy(self, instance):
        instance.delete()
