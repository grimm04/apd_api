from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import TelegramGroup , EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, TelegramGroupFilter

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination


# Create your views here.
class TelegramGroupViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TelegramGroup.objects.all()
    serializer_class = serializers.TelegramGroupSerializers
    # update_serializer_class = serializers.UDDepartemenSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TelegramGroupFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_telegram_group']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Master - Fasop - Telegram Group.",
        description="Get Data Master - Fasop - Telegram Group.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_fasop']
    )
    def list(self, request):
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title        = 'Telegram Group'

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'telegram_group.view',headers=header, relation=relation, fields=fields,title=title) 

    @extend_schema(
        methods=["POST"],
        summary="Create Data Master - Fasop - Telegram Group.",
        description="Create Data Master - Fasop - Telegram Group.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_fasop']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'telegram_group.create')

    @extend_schema(
        methods=["GET"],
        summary="Display Specified Master - Fasop - Telegram Group.",
        description="Get Details Master - Fasop - Telegram Group.",
        tags=['master_fasop']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        telegram_group = self.queryset.filter(id_telegram_group=pk)
        if telegram_group is None:
            return not_found('telegram_group.not_found')

        serializer = self.serializer_class(telegram_group, many=True)
        return response__(request, serializer, 'telegram_group.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Master - Fasop - Telegram Group.",
        description="Update Data Master - Fasop - Telegram Group.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_fasop']
    )
    def update(self, request, pk):
        telegram_group = get_object_or_404(TelegramGroup, pk=pk)
        serializer = self.serializer_class(instance=telegram_group, data=request.data)

        return post_update_response(serializer, 'telegram_group.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Master - Fasop - Telegram Group.",
        description="Delete Data Master - Fasop - Telegram Group.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_fasop']
    )
    def destroy(self, request, pk):
        telegram_group = get_object_or_404(TelegramGroup, pk=pk)
        self.perform_destroy(telegram_group)
        return response__(request, telegram_group, 'telegram_group.delete')

    def perform_destroy(self, instance):
        instance.delete()
