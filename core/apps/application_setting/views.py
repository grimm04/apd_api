from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.views import APIView 
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import ApplicationSetting
from .filters import ApplicationSettingFilter, SearchFilter, ApplicationSetting

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination 

class ApplicationSettingViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = ApplicationSetting.objects.all()
    serializer_class = serializers.CRApplicationSettingSerializers
    update_serializer_class = serializers.UDApplicationSettingSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = ApplicationSettingFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['app_name','email','app_name_short']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_app']

    @extend_schema(
        methods=["GET"],
        summary="Get Application Setting.",
        description="Get Application Setting.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['application setting']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'application_setting.view')

    @extend_schema(
        methods=["POST"],
        summary="Create Application Setting.",
        description="Create Application Setting.",
        request=serializer_class,
        responses=serializer_class,
        tags=['application setting']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'application_setting.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Application Setting (Specified).",
        description="Get Application Setting (Specified).",
        tags=['application setting']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        application_setting = self.queryset.filter(id_app=pk)
        if not application_setting:
            return not_found('application_setting.not_found')

        serializer = self.serializer_class(application_setting, many=True)
        return response__(request, serializer, 'application_setting.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Application Setting",
        description="Update Application Setting",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['application setting']
    )
    def update(self, request, pk):
        application_setting = get_object_or_404(ApplicationSetting, pk=pk)
        serializer = self.update_serializer_class(instance=application_setting, data=request.data)

        return post_update_response(serializer, 'application_setting.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Application Setting.",
        description="Delete Application Setting.",
        request=serializer_class,
        responses=serializer_class,
        tags=['application setting']
    )
    def destroy(self, request, pk):
        application_setting = get_object_or_404(ApplicationSetting, pk=pk)
        self.perform_destroy(application_setting)
        return response__(request, application_setting, 'application_setting.delete')

    def perform_destroy(self, instance):
        instance.delete()


class ApplicationSettingByIDViews(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    serializer_class = serializers.GetConfig
    queryset = ApplicationSetting.objects.all()  

    @extend_schema(
        methods=["GET"],
        summary="Get Application Setting (Specified).",
        description="Get Application Setting (Specified).",
        tags=['application setting get detail']
    )
    def get(self, request, pk, *args, **kwargs):
        application_setting = self.queryset.filter(id_app=pk)
        if not application_setting:
            return not_found('application_setting.not_found')

        serializer = self.serializer_class(application_setting, many=True)
        return response__(request, serializer, 'application_setting.view')