import datetime
import json
import os
import re
from imp import PKG_DIRECTORY
from django.conf import settings
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, response, status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.decorators import action
from library.api_response import ApiResponse, build_response
from drf_spectacular.utils import extend_schema, OpenApiParameter
from django.http import HttpResponse, Http404
from base.response import response__, get_response, post_update_response, not_found, response_basic, exists
from base.custom_pagination import CustomPagination

class BackupHarianViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    @extend_schema(
        methods=["GET"],
        summary="Get OPSISDIS - Frekuensi Pembangkit - Backup Harian - List File",
        description="Get OPSISDIS - Frekuensi Pembangkit - Backup Harian - List File",
        parameters=[
            OpenApiParameter(name='date', description=f'date example: {datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m")}',
                             required=True, type=str,
                             default=datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m')),
        ],
        tags=['opsisdis_frekuensi']
    )
    @action(detail=False, url_path='list-file', url_name='list-file')
    def list_file(self, request):
        date = request.GET.get('date')
        file_path = os.listdir(os.path.join(settings.MEDIA_ROOT_FREKWENSI, '{}'.format(date)))
        result = []
        for data in file_path:
            data_dict = {
                'filename': data,
                'filepath': date,
                'fileurl': f'opsisdis/frekuensi/backup-harian/download-file?filepath={date}&filename={data}'
            }
            result.append(data_dict)

        return response.Response({
            "status": status.HTTP_200_OK,
            "message": 'Berhasil Mendapatkan Data',
            "results": result
        })

    @extend_schema(
        methods=["GET"],
        summary="Get OPSISDIS - Frekuensi Pembangkit - Backup Harian - List Directory",
        description="Get OPSISDIS - Frekuensi Pembangkit - Backup Harian - List Directory",
        parameters=[],
        tags=['opsisdis_frekuensi']
    )
    @action(detail=False, url_path='list-directory', url_name='list-directory')
    def list_directory(self, request):
        file_path = [f.path for f in os.scandir(settings.MEDIA_ROOT_FREKWENSI) if f.is_dir()]
        result = []
        for data in file_path:
            directory_name = re.sub('.*/', '', data)
            directory_name = re.sub('.*\\\\', '', directory_name)
            data_dict = {
                'directory_name': f'{directory_name}',
            }
            result.append(data_dict)

        return response.Response({
            "status": status.HTTP_200_OK,
            "message": 'Berhasil Mendapatkan Data',
            "results": result
        })

    @extend_schema(
        tags=['opsisdis_frekuensi'],
        parameters=[
            OpenApiParameter(name='filepath', description='filepath', required=True, type=str),
            OpenApiParameter(name='filename', description='filename', required=True, type=str)
        ]
    )
    @action(methods=['get'], detail=False, url_path='download-file', url_name='download-file')
    def download_file(self, request):
        try:
            filename = request.GET.get('filename')
            filepath = request.GET.get('filepath')
            file_path = os.path.join(settings.MEDIA_ROOT_FREKWENSI, filepath, filename)
            response = HttpResponse(open(file_path, 'rb'), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'attachment; filename="%s"' % filename
            return response
        except:
            return build_response(ApiResponse(message='files not found'))