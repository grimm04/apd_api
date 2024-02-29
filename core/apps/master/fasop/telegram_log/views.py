from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import TelegramLog , EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, TelegramLogFilter

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination


# Create your views here.
class TelegramLogViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TelegramLog.objects.all()
    serializer_class = serializers.TelegramLogSerializers
    # update_serializer_class = serializers.UDDepartemenSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TelegramLogFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['msg']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Master - Fasop - Telegram Log.",
        description="Get Data Master - Fasop - Telegram Log.",
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
        title        = 'Telegram Log'

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'telegram_log.view',headers=header, relation=relation, fields=fields,title=title) 

    @extend_schema(
        methods=["POST"],
        summary="Create Data Master - Fasop - Telegram Log.",
        description="Create Data Master - Fasop - Telegram Log.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_fasop']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'telegram_log.create')

    @extend_schema(
        methods=["GET"],
        summary="Display Specified Master - Fasop - Telegram Log.",
        description="Get Details Master - Fasop - Telegram Log.",
        tags=['master_fasop']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        telegram_group = self.queryset.filter(id=pk)
        if telegram_group is None:
            return not_found('telegram_log.not_found')

        serializer = self.serializer_class(telegram_group, many=True)
        return response__(request, serializer, 'telegram_log.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Master - Fasop - Telegram Log.",
        description="Update Data Master - Fasop - Telegram Log.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_fasop']
    )
    def update(self, request, pk):
        telegram_group = get_object_or_404(TelegramLog, pk=pk)
        serializer = self.serializer_class(instance=telegram_group, data=request.data)

        return post_update_response(serializer, 'telegram_log.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Master - Fasop - Telegram Log.",
        description="Delete Data Master - Fasop - Telegram Log.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_fasop']
    )
    def destroy(self, request, pk):
        telegram_group = get_object_or_404(TelegramLog, pk=pk)
        self.perform_destroy(telegram_group)
        return response__(request, telegram_group, 'telegram_log.delete')

    def perform_destroy(self, instance):
        instance.delete()
