import jwt
import hashlib
from django.shortcuts import get_object_or_404
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import ExtUserToken
from . import serializers
from .filters import SearchFilter, ExtUserTokenFilter

from base.response import response__, get_response, post_update_response, not_found, \
    response_basic, post_update_response_token
from base.custom_pagination import CustomPagination


# Create your views here.
class ExtUserTokenViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = ExtUserToken.objects.all()
    serializer_class = serializers.ExtUserTokenSerializers
    update_serializer_class = serializers.UpdateExtUserTokenSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = ExtUserTokenFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_token']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Master - External - Ext User Token.",
        description="Get Data Master - External - Ext User Token.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['external']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'ext_user_token.view')

    @extend_schema(
        methods=["POST"],
        summary="Create Data Master - External - Ext User Token.",
        description="Create Data Master - External - Ext User Token.",
        request=serializer_class,
        responses=serializer_class,
        tags=['external']
    )
    # create
    def create(self, request):
        data = request.data
        hash_object = hashlib.sha1(str(data['nama']).encode('utf-8'))
        token = hash_object.hexdigest()
        data['token'] = token  
        
        serializer = self.serializer_class(data=data) 
        return post_update_response(serializer, 'ext_user_token.create')

        # ext_user_token = get_object_or_404(ExtUserToken, pk=data_save['id_token'])
        # data_token = {
        #     'id_token': data_save['id_token'],
        #     'id_user': data_save['id_user'],
        # }
        
        
        # token = jwt.encode(data_token, settings.SECRET_KEY, algorithm="HS256")
        # update_serializer = self.update_serializer_class(instance=ext_user_token, data={'token': pbHash})
        # return post_update_response(update_serializer, 'ext_user_token.update_add')

    @extend_schema(
        methods=["GET"],
        summary="Display Specified Master - External - Ext User Token.",
        description="Get Details Master - External - Ext User Token.",
        tags=['external']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ext_user_token = self.queryset.filter(id_token=pk)
        if ext_user_token is None:
            return not_found('ext_user_token.not_found')

        serializer = self.serializer_class(ext_user_token, many=True)
        return response__(request, serializer, 'ext_user_token.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Master - External - Ext User Token.",
        description="Update Data Master - External - Ext User Token.",
        request=serializer_class,
        responses=serializer_class,
        tags=['external']
    )
    def update(self, request, pk):
        ext_user_token = get_object_or_404(ExtUserToken, pk=pk)
        serializer = self.serializer_class(instance=ext_user_token, data=request.data)

        return post_update_response(serializer, 'ext_user_token.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Master - External - Ext User Token.",
        description="Delete Data Master - External - Ext User Token.",
        request=serializer_class,
        responses=serializer_class,
        tags=['external']
    )
    def destroy(self, request, pk):
        ext_user_token = get_object_or_404(ExtUserToken, pk=pk)
        self.perform_destroy(ext_user_token)
        return response__(request, ext_user_token, 'ext_user_token.delete')

    def perform_destroy(self, instance):
        instance.delete()
