import re

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import Group, GroupAccess
from library.api_response import ApiResponse, build_response

class GroupEndpointViews(viewsets.GenericViewSet):

    model = Group()

    @extend_schema(
        methods=["POST"],
        summary="Create Group.",
        description="Create Group.",
        parameters=[
            OpenApiParameter(name='nama_group', description='nama_group', required=True, type=str),
            OpenApiParameter(name='status', description='status', required=True, type=int, default=1),
        ],
        tags=['group']
    )
    def create(self, request):
        try:
            nama_group = request.query_params.get('nama_group')
            _status = request.query_params.get('status')

            data = {
                'nama_group': nama_group,
                'status': _status
            }
            _, message = self.model.create_group(data)
            if not _:
                raise Exception('failed to save group: {}'.format(message))

            return build_response(ApiResponse(status=True))
        except Exception as e:
            return build_response(ApiResponse(message=str(e)))

    @extend_schema(
        methods=["GET"],
        summary="Get List Group.",
        description="Get List Group.",
        parameters=[
            OpenApiParameter(name='keyword', description='keyword', required=False, type=str),
            OpenApiParameter(name='start', description='start', required=False, type=str, default=0),
            OpenApiParameter(name='rows', description='rows', required=False, type=str, default=10),
            OpenApiParameter(name='order_by', description='order by', required=True, type=str, default='id'),
        ],
        tags=['group']
    )
    def list(self, request):
        try:
            keyword = request.GET.get('keyword')
            start = request.GET.get('start')
            rows = request.GET.get('rows')
            order_by = request.GET.get('order_by', 'id')

            _, data = self.model.read_group(keyword, start, rows, order_by)
            if not _:
                raise Exception('failed to get data group: {}'.format(data))

            return build_response(ApiResponse(status=True, data=data))
        except Exception as e:
            return build_response(ApiResponse(message=str(e)))

    @extend_schema(
        methods=["GET"],
        summary="Get Group.",
        description="Get Group.",
        tags=['group']
    )
    def retrieve(self, request, pk):
        try:
            _, data = self.model.read_group_detail(pk=pk)
            if not _:
                raise Exception('failed to save group: {}'.format(data))

            return build_response(ApiResponse(status=True, data=data))
        except Exception as e:
            return build_response(ApiResponse(message=str(e)))

    @extend_schema(
        methods=["PUT"],
        summary="Update Group.",
        description="Update Group.",
        parameters=[
            OpenApiParameter(name='nama_group', description='nama_group', required=False, type=str),
            OpenApiParameter(name='status', description='status', required=False, type=int)
        ],
        tags=['group']
    )
    def update(self, request, pk):
        try:
            data_update = dict()
            for param in request.query_params:
                data_update[param] = request.query_params.get(param)

            if not data_update:
                raise Exception('nothing to be update')

            _, message = self.model.update_group(data_update, pk)
            if not _:
                raise Exception('failed to update group: {}'.format(message))

            return build_response(ApiResponse(status=True))
        except Exception as e:
            return build_response(ApiResponse(message=str(e)))

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Group.",
        description="Delete Group.",
        tags=['group']
    )
    def destroy(self, request, pk):
        try:
            _, message = self.model.delete_group(pk)
            if not _:
                raise Exception('failed to delete group: {}'.format(message))

            return build_response(ApiResponse(status=True))
        except Exception as e:
            return build_response(ApiResponse(message=str(e)))

class GroupAccessEndpointViews(viewsets.GenericViewSet):

    model = GroupAccess()

    @extend_schema(
        methods=["POST"],
        summary="Create Group Access.",
        description="Create Group Access.",
        parameters=[
            OpenApiParameter(name='id_user', description='id_user', required=True, type=int),
            OpenApiParameter(name='id_group', description='id_group', required=True, type=int),
            OpenApiParameter(name='status', description='status', required=True, type=int, default=1),
        ],
        tags=['group']
    )
    def create(self, request):
        try:
            id_user = request.query_params.get('id_user')
            id_group = request.query_params.get('id_group')
            _status = request.query_params.get('status')

            data = {
                'id_user': id_user,
                'id_group': id_group,
                'status': _status
            }
            _, message = self.model.create_group_access(data)
            if not _:
                raise Exception('failed to save group access: {}'.format(message))

            return build_response(ApiResponse(status=True))
        except Exception as e:
            return build_response(ApiResponse(message=str(e)))

    @extend_schema(
        methods=["GET"],
        summary="Get User Group Access.",
        description="Get User Group Access.",
        tags=['group']
    )
    def retrieve(self, request, pk):
        try:
            _, data = self.model.read_group_detail_access(pk=pk)
            if not _:
                raise Exception('failed to save group access: {}'.format(data))

            return build_response(ApiResponse(status=True, data=data))
        except Exception as e:
            return build_response(ApiResponse(message=str(e)))

    @extend_schema(
        methods=["GET"],
        summary="Get List Group Access.",
        description="Get List Group Access.",
        parameters=[
            OpenApiParameter(name='keyword', description='keyword', required=False, type=str),
            OpenApiParameter(name='start', description='start', required=False, type=str, default=0),
            OpenApiParameter(name='rows', description='rows', required=False, type=str, default=10),
            OpenApiParameter(name='order_by', description='order by', required=True, type=str, default='id'),
        ],
        tags=['group']
    )
    def list(self, request):
        try:
            keyword = request.GET.get('keyword')
            start = request.GET.get('start')
            rows = request.GET.get('rows')
            order_by = request.GET.get('order_by', 'id')

            _, data = self.model.read_group_access(keyword, start, rows, order_by)
            if not _:
                raise Exception('failed to get data group: {}'.format(data))

            return build_response(ApiResponse(status=True, data=data))
        except Exception as e:
            return build_response(ApiResponse(message=str(e)))

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Group.",
        description="Delete Group.",
        parameters=[
            OpenApiParameter(name='id_group', description='id_group', required=True, type=int)
        ],
        tags=['group']
    )
    def destroy(self, request, pk):
        try:
            id_group = request.query_params.get('id_group')
            _, message = self.model.delete_group_access(pk, id_group)
            if not _:
                raise Exception('failed to delete group access: {}'.format(message))

            return build_response(ApiResponse(status=True))
        except Exception as e:
            return build_response(ApiResponse(message=str(e)))