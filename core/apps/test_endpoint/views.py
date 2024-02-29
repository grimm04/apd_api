import re

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import Menu, MenuAkses
from library.api_response import ApiResponse, build_response


class TestMenuViews(viewsets.GenericViewSet):

    @extend_schema(
        methods=["POST"],
        summary="Create Menu.",
        description="Create Menu.",
        parameters=[
            OpenApiParameter(name='nama_menu', description='nama_menu', required=True, type=str),
            OpenApiParameter(name='display_menu', description='display_menu', required=True, type=str),
            OpenApiParameter(name='icon', description='icon', required=True, type=str),
            OpenApiParameter(name='sorting_no', description='sorting_no', required=True, type=int, default=1),
            OpenApiParameter(name='url', description='url', required=True, type=str),
            OpenApiParameter(name='status', description='status', required=True, type=int, default=1),
            OpenApiParameter(name='child_menu', description='child_menu', required=True, type=int, default=0),
            OpenApiParameter(name='keterangan', description='keterangan', required=False, type=str),
            OpenApiParameter(name='parent_id', description='parent_id', required=False, type=int),
        ],
        tags=['test_menu']
    )
    def create(self, request):
        model = Menu()
        try:
            nama_menu = request.query_params.get('nama_menu')
            display_menu = request.query_params.get('display_menu')
            icon = request.query_params.get('icon')
            sorting_no = request.query_params.get('sorting_no')
            url = request.query_params.get('url')
            _status = request.query_params.get('status')
            child_menu = request.query_params.get('child_menu')
            keterangan = request.query_params.get('keterangan')
            parent_id = request.query_params.get('parent_id')

            data = {
                'nama_menu': nama_menu,
                'display_menu': display_menu,
                'icon': icon,
                'sorting_no': sorting_no,
                'url': url,
                'status': _status,
                'child_menu': child_menu,
                'keterangan': keterangan,
                'parent_id': parent_id,
            }
            _, message = model.create_menu(data)
            if not _:
                raise Exception('failed to save menu: {}'.format(message))

            return build_response(ApiResponse(status=True))
        except Exception as e:
            return build_response(ApiResponse(message=str(e)))

    @extend_schema(
        methods=["GET"],
        summary="Get List Menu.",
        description="Get List Menu.",
        parameters=[
            OpenApiParameter(name='keyword', description='keyword', required=False, type=str),
            OpenApiParameter(name='start', description='start', required=False, type=str, default=0),
            OpenApiParameter(name='rows', description='rows', required=False, type=str, default=10),
            OpenApiParameter(name='order_by', description='order by', required=True, type=str, default='id'),
        ],
        tags=['test_menu']
    )
    def list(self, request):
        model = Menu()
        try:
            keyword = request.GET.get('keyword')
            start = request.GET.get('start')
            rows = request.GET.get('rows')
            order_by = request.GET.get('order_by', 'id')

            _, data = model.read_menu(keyword, start, rows, order_by)
            if not _:
                raise Exception('failed to get data menu: {}'.format(data))

            return build_response(ApiResponse(status=True, data=data))
        except Exception as e:
            return build_response(ApiResponse(message=str(e)))

    @extend_schema(
        methods=["GET"],
        summary="Get Menu.",
        description="Get Menu.",
        tags=['test_menu']
    )
    def retrieve(self, request, pk):
        model = Menu()
        try:
            _, data = model.read_menu_detail(pk=pk)
            if not _:
                raise Exception('failed to save menu: {}'.format(data))

            return build_response(ApiResponse(status=True, data=data))
        except Exception as e:
            return build_response(ApiResponse(message=str(e)))

    @extend_schema(
        methods=["PUT"],
        summary="Update Menu.",
        description="Update Menu.",
        parameters=[
            OpenApiParameter(name='nama_menu', description='nama_menu', required=False, type=str),
            OpenApiParameter(name='display_menu', description='display_menu', required=False, type=str),
            OpenApiParameter(name='icon', description='icon', required=False, type=str),
            OpenApiParameter(name='sorting_no', description='sorting_no', required=False, type=int),
            OpenApiParameter(name='url', description='url', required=False, type=str),
            OpenApiParameter(name='status', description='status', required=False, type=int),
            OpenApiParameter(name='child_menu', description='child_menu', required=False, type=int),
            OpenApiParameter(name='keterangan', description='keterangan', required=False, type=str),
            OpenApiParameter(name='parent_id', description='parent_id', required=False, type=int),
        ],
        tags=['test_menu']
    )
    def update(self, request, pk):
        model = Menu()
        try:
            data_update = dict()
            for param in request.query_params:
                data_update[param] = request.query_params.get(param)

            if not data_update:
                raise Exception('nothing to be update')

            _, message = model.update_menu(data_update, pk)
            if not _:
                raise Exception('failed to update menu: {}'.format(message))

            return build_response(ApiResponse(status=True))
        except Exception as e:
            return build_response(ApiResponse(message=str(e)))

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Menu.",
        description="Delete Menu.",
        tags=['test_menu']
    )
    def destroy(self, request, pk):
        model = Menu()
        try:
            _, message = model.delete_menu(pk)
            if not _:
                raise Exception('failed to delete menu: {}'.format(message))

            return build_response(ApiResponse(status=True))
        except Exception as e:
            return build_response(ApiResponse(message=str(e)))


class TestMenuAccessViews(viewsets.GenericViewSet):

    @extend_schema(
        methods=["POST"],
        summary="Create Menu Access.",
        description="Create Menu Access.",
        parameters=[
            OpenApiParameter(name='id_menu', description='nama_menu', required=True, type=int),
            OpenApiParameter(name='id_group', description='display_menu', required=True, type=int),
            OpenApiParameter(name='lihat', description='icon (0=false/1=true, default: 1)', required=False, type=int),
            OpenApiParameter(name='tambah', description='sorting_no (0=false/1=true, default: 1)',
                             required=False, type=int),
            OpenApiParameter(name='edit', description='url (0=false/1=true, default: 1)', required=False, type=int),
            OpenApiParameter(name='hapus', description='status (0=false/1=true, default: 1)', required=False, type=int),
        ],
        tags=['test_menu']
    )
    def create(self, request):
        model = MenuAkses()
        try:
            data_insert = dict()
            for param in request.query_params:
                data_insert[param] = request.query_params.get(param)

            if not data_insert:
                raise Exception('nothing to be save')

            _, message = model.create_menu_access(data_insert)
            if not _:
                raise Exception('failed to save menu  access: {}'.format(message))

            return build_response(ApiResponse(status=True))
        except Exception as e:
            return build_response(ApiResponse(message=str(e)))

    @extend_schema(
        methods=["GET"],
        summary="Get List Menu Access.",
        description="Get List Menu Access.",
        parameters=[
            OpenApiParameter(name='keyword', description='keyword', required=False, type=str),
            OpenApiParameter(name='start', description='start', required=False, type=str, default=0),
            OpenApiParameter(name='rows', description='rows', required=False, type=str, default=10),
            OpenApiParameter(name='order_by', description='order by', required=True, type=str, default='id ASC'),
        ],
        tags=['test_menu']
    )
    def list(self, request):
        model = MenuAkses()
        try:
            keyword = request.GET.get('keyword')
            start = request.GET.get('start')
            rows = request.GET.get('rows')
            order_by = request.GET.get('order_by', 'id')

            _, data = model.read_menu_access(keyword, start, rows, order_by)
            if not _:
                raise Exception('failed to get data menu: {}'.format(data))

            return build_response(ApiResponse(status=True, data=data))
        except Exception as e:
            return build_response(ApiResponse(message=str(e)))

    @extend_schema(
        methods=["GET"],
        summary="Get Menu Access.",
        description="Get Menu Access.",
        tags=['test_menu']
    )
    def retrieve(self, request, pk):
        model = MenuAkses()
        try:
            _, data = model.read_menu_detail_access(pk=pk)
            if not _:
                raise Exception('failed to get menu: {}'.format(data))

            return build_response(ApiResponse(status=True, data=data))
        except Exception as e:
            return build_response(ApiResponse(message=str(e)))

    @extend_schema(
        methods=["PUT"],
        summary="Update Menu Access.",
        description="Update Menu Access.",
        parameters=[
            OpenApiParameter(name='id_menu', description='nama_menu', required=False, type=int),
            OpenApiParameter(name='id_group', description='display_menu', required=False, type=int),
            OpenApiParameter(name='lihat', description='icon (0=false/1=true, default: 1)', required=False, type=int),
            OpenApiParameter(name='tambah', description='sorting_no (0=false/1=true, default: 1)',
                             required=False, type=int),
            OpenApiParameter(name='edit', description='url (0=false/1=true, default: 1)', required=False, type=int),
            OpenApiParameter(name='hapus', description='status (0=false/1=true, default: 1)', required=False, type=int),
        ],
        tags=['test_menu']
    )
    def update(self, request, pk):
        model = MenuAkses()
        try:
            data_update = dict()
            for param in request.query_params:
                data_update[param] = request.query_params.get(param)

            if not data_update:
                raise Exception('nothing to be update')

            _, message = model.update_menu_access(data_update, pk)
            if not _:
                raise Exception('failed to update menu: {}'.format(message))

            return build_response(ApiResponse(status=True))
        except Exception as e:
            return build_response(ApiResponse(message=str(e)))

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Menu Access.",
        description="Delete Menu Access.",
        tags=['test_menu']
    )
    def destroy(self, request, pk):
        model = MenuAkses()
        try:
            _, message = model.delete_menu_access(pk)
            if not _:
                raise Exception('failed to delete menu: {}'.format(message))

            return build_response(ApiResponse(status=True))
        except Exception as e:
            return build_response(ApiResponse(message=str(e)))
