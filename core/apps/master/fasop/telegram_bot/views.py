from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import TelegramBot , EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, TelegramBotFilter

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination


# Create your views here.
class TelegramBotViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TelegramBot.objects.all()
    serializer_class = serializers.TelegramBotSerializers
    # update_serializer_class = serializers.UDDepartemenSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TelegramBotFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['name']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_telegram_bot']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Master - Fasop - Telegram Bot.",
        description="Get Data Master - Fasop - Telegram Bot.",
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
        title        = 'Telegram Bot'

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'telegram_bot.view',headers=header, relation=relation, fields=fields,title=title)  

    @extend_schema(
        methods=["POST"],
        summary="Create Data Master - Fasop - Telegram Bot.",
        description="Create Data Master - Fasop - Telegram Bot.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_fasop']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'telegram_bot.create')

    @extend_schema(
        methods=["GET"],
        summary="Display Specified Master - Fasop - Telegram Bot.",
        description="Get Details Master - Fasop - Telegram Bot.",
        tags=['master_fasop']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        telegram_bot = self.queryset.filter(id_telegram_bot=pk)
        if telegram_bot is None:
            return not_found('telegram_bot.not_found')

        serializer = self.serializer_class(telegram_bot, many=True)
        return response__(request, serializer, 'telegram_bot.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Master - Fasop - Telegram Bot.",
        description="Update Data Master - Fasop - Telegram Bot.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_fasop']
    )
    def update(self, request, pk):
        telegram_bot = get_object_or_404(TelegramBot, pk=pk)
        serializer = self.serializer_class(instance=telegram_bot, data=request.data)

        return post_update_response(serializer, 'telegram_bot.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Master - Fasop - Telegram Bot.",
        description="Delete Data Master - Fasop - Telegram Bot.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_fasop']
    )
    def destroy(self, request, pk):
        telegram_bot = get_object_or_404(TelegramBot, pk=pk)
        self.perform_destroy(telegram_bot)
        return response__(request, telegram_bot, 'telegram_bot.delete')

    def perform_destroy(self, instance):
        instance.delete()
