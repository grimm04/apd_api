import os
import pandas as pd
from openpyxl import load_workbook
import xlsxwriter
from datetime import datetime
from django.http import HttpResponse, Http404
from django.conf import settings
from rest_framework import viewsets, renderers
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, OpenApiParameter
from apps.master.jaringan.ref_lokasi import serializers
from apps.master.management_upload.models import managementUpload
from library.api_response import ApiResponse, build_response
from base.excel_template import template, status_listrik,  fillnan
from apps.master.jaringan.ref_lokasi.models import RefLokasi, RefLokasiTempDelete

from ..write_row import add_new_sheet
from .models import EXPORT_HEADERS, EXPORT_HEADERS_DATA 
class GarduHubungView(viewsets.GenericViewSet):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefLokasi.objects.filter(id_ref_jenis_lokasi=11)

    serializer_class = serializers.RefLokasiSerializer
    create_serializer_class = serializers.CRRefLokasiSerializers
    update_serializer_class = serializers.UDRefLokasiSerializers

    model = managementUpload()

    @extend_schema(
        tags=['master_management_upload'],
        summary="Management Upload SLD - Download Data Excel Gardu Hubung",
        description="Management Upload SLD - Download Data Excel Gardu Hubung",
    )
    @action(methods=['get'], detail=False, url_path='download-excel', url_name='download-excel')
    def download_excel(self, request):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            if not serializer.data:
                return build_response(ApiResponse(message=str('empty')))
            file_path = os.path.join(settings.MEDIA_ROOT, 'LAP MASTER GARDU HUBUNG.xlsx')
            workbook = xlsxwriter.Workbook(file_path)
            ws_acc = workbook.add_worksheet('DATA GARDU HUBUNG')
            format = workbook.add_format()
            format.set_bg_color('#D3D3D3')
            format.set_align('left')
            add_new_sheet(worksheet=ws_acc,headers=EXPORT_HEADERS_DATA,format=format)   
            index = 1
            for message in serializer.data:
                status = message['status_listrik']
                if status == '0':
                    status = 'inactive'
                elif status == '1':
                    status = 'active'
                if message.get('id_uid'):
                    uid = message.get('id_uid', {}).get('nama_lokasi')
                else:
                    uid = ''
                if message.get('id_up3_1'):
                    up3_1 = message.get('id_up3_1', {}).get('nama_lokasi')
                else:
                    up3_1 = ''
                if message.get('id_ulp'):
                    ulp = message.get('id_ulp', {}).get('nama_lokasi')
                else:
                    ulp = ''
                if message.get('parent_lokasi'):
                    id_parent_lokasi = message.get('parent_lokasi', {}).get('id_ref_lokasi')
                    name_parent_lokasi = message.get('parent_lokasi', {}).get('nama_lokasi')
                else:
                    id_parent_lokasi = ''
                    name_parent_lokasi = ''

                ws_acc.write(index, 0, str(message['id_ref_lokasi']))
                ws_acc.write(index, 1, message['nama_lokasi'])
                ws_acc.write(index, 2, message['alamat'])
                # ws_acc.write(index, 3, id_parent_lokasi)
                # ws_acc.write(index, 4, name_parent_lokasi)
                ws_acc.write(index, 3, message['lat'])
                ws_acc.write(index, 4, message['lon'])
                # ws_acc.write(index, 7, uid)
                # ws_acc.write(index, 8, up3_1)
                # ws_acc.write(index, 9, ulp)
                ws_acc.write(index, 5, status)
                index += 1
            workbook.close()
            response = HttpResponse(open(file_path, 'rb'), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(file_path)
            return response
        except:
            return build_response(ApiResponse(message='files not found'))