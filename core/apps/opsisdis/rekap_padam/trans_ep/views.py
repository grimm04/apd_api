from tkinter import E
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
import datetime

import pandas as pd
import os 
import xlsxwriter
from django.conf import settings
from apps.master.management_upload.write_row import add_new_sheet

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework import response,status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from dateutil import parser 
from rest_framework.decorators import action
from django.http import HttpResponse
from apps.opsisdis.rekap_padam.trans_ep_section.serializers import CRTransEpSectionSerializers,UDTransEpSectionSerializers,GetTransEpSerializers
from apps.opsisdis.rekap_padam.trans_ep_section.models import TransEpSection 
from library.api_response import ApiResponse, build_response
 
from . import serializers
from .models import TransEp ,EXPORT_HEADERS_TRANS_EP
from apps.opsisdis.rekap_padam.trans_ep_peralatan.models import TransEpPeralatan ,EXPORT_HEADERS,EXPORT_HEADERS_CAPTION,EXPORT_FIELDS,EXPORT_RELATION_FIELD 
from apps.opsisdis.rekap_padam.trans_ep_peralatan.serializers import ExportTransEpPeralatanSerializers 
from apps.opsisdis.rekap_padam.trans_ep_peralatan.filters import TransEpPeralatanFilter 
from .filters import TransEpFilter, SearchFilter, TransEp,PeralatanFilter

from base.response import response__, get_response, post_update_response, not_found,response_retreve,validate_serializer,error_response,response_json
from base.custom_pagination import CustomPagination 
from base.negotiation import CustomContentNegotiation
from apps.master.jaringan.ref_lokasi.models import RefLokasi   


class TransEpViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TransEp.objects.all()
    queryset_ref_lokasi = RefLokasi.objects.all() 
    serializer_class = serializers.TransEpSerializers
    all_serializer_class = serializers.AllNorelationTransEpSerializers
    create_serializer_class = serializers.CRTransEpSerializers
    update_serializer_class = serializers.UDTransEpSerializers
    # update_status_serializer_class = serializers.UDStatusTransEpSerializers 
    get_peralatan_detail_serializer_class = serializers.ReflokasiPeralatanSerializers
    get_hitung_ens_serializer_class = serializers.TransEpHitungENSSerializers
    ep_section_serializer_class = CRTransEpSectionSerializers
    ep_section_update_serializer_class = UDTransEpSectionSerializers
    ep_get_ens_serializer = GetTransEpSerializers
    content_negotiation_class = CustomContentNegotiation

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TransEpFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['no_apkt','no_event', 'id_up3_id__nama_lokasi','id_ulp_id__nama_lokasi']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_ep']
    def getNoEvent(self):  
        date = datetime.date.today()   
        month = date.month
        year = date.year 
        no_event = TransEp.objects.filter(tanggal__month=month,tanggal__year=year).count()   
        if not no_event:
            nf = str(1).zfill(5)
        new_event_i = str(no_event + 1).zfill(5)
        # 00000+no/bln/thn/OPSISDIS 
        new_ne = str(new_event_i) + '/' + str(month)+ '/' + str(year)+ '/OPSISDIS'
        return new_ne 

    # Export
    def export(self, queryset=None, filter=None):
        # try: 
            # serializer = self.get_serializer(queryset, many=True) 
            # if not serializer.data:
            #     return build_response(ApiResponse(message=str('empty')))
 
            file_path = os.path.join(settings.MEDIA_ROOT, 'Rekap Padam.xlsx')
            workbook = xlsxwriter.Workbook(file_path)
            ws_acc = workbook.add_worksheet('Data Rekap Padam')
            ws_acc.set_row(1, 30)
            format = workbook.add_format()
            format.set_bg_color('yellow')
            format.set_align('center')
            format.set_align('vcenter')
            format.set_border(1)
            # add_new_sheet(worksheet=ws_acc,headers=EXPORT_HEADERS_TRANS_EP,format=format) 
            ws_acc.set_tab_color('yellow')
            ws_acc.set_column('A:A', 5)
            ws_acc.set_column('B:B', 20)
            ws_acc.set_column('C:C', 20)
            ws_acc.set_column('D:D', 30)
            ws_acc.set_column('E:E', 30)
            ws_acc.set_column('F:F', 10)
            ws_acc.set_column('G:G', 20)
            ws_acc.set_column('H:H', 30)
            ws_acc.set_column('I:I', 30)
            ws_acc.set_column('J:J', 30)
            ws_acc.set_column('K:K', 30)
            ws_acc.set_column('L:L', 20)
            ws_acc.set_column('M:M', 20)
            ws_acc.set_column('N:N', 20)
            ws_acc.set_column('O:O', 30) 
            ws_acc.set_column('P:P', 20)
            ws_acc.set_column('Q:Q', 10)
            ws_acc.set_column('R:R', 10)
            ws_acc.set_column('S:S', 10)
            ws_acc.set_column('T:T', 10)
            ws_acc.set_column('U:U', 20)
            ws_acc.set_column('V:V', 30)
            ws_acc.set_column('W:W', 10)
            ws_acc.set_column('X:X', 10)
            ws_acc.set_column('Y:Y', 30)
            ws_acc.set_column('Z:Z', 40)
            ws_acc.set_column('AA:AA', 40)
            ws_acc.set_column('AB:AB', 40)
            ws_acc.set_column('AC:AC', 40)
            ws_acc.set_column('AC:AC', 30)
            ws_acc.set_column('AE:AE', 40)
            ws_acc.set_column('AF:AF', 40)
            ws_acc.set_column('AG:AG', 10)
            ws_acc.set_column('AH:AH', 10)
            ws_acc.set_column('AI:AI', 20)
            ws_acc.set_column('AJ:AJ', 20)
            ws_acc.set_column('AK:AK', 40)
            ws_acc.set_column('AL:AL', 20)
            ws_acc.set_column('AM:AM', 20)
            ws_acc.set_column('AN:AN', 20)
            ws_acc.set_column('AO:AO', 40)
            ws_acc.set_column('AP:AP', 30)
            ws_acc.set_column('AQ:AQ', 40)
            ws_acc.set_column('AR:AR', 20)
            ws_acc.set_column('AS:AS', 20)
            ws_acc.set_column('AT:AT', 30)
            ws_acc.set_column('AU:AU', 30)
            ws_acc.set_column('AV:AV', 30)
            ws_acc.set_column('AW:AW', 30)
            ws_acc.set_column('AX:AX', 30)
            ws_acc.set_column('AY:AY', 30)
            ws_acc.set_column('AZ:AZ', 20)
            ws_acc.set_column('BA:BA', 30)
            ws_acc.set_column('BB:BB', 30)
            ws_acc.set_column('BC:BC', 40)
            ws_acc.set_column('BD:BD', 40)
            ws_acc.set_column('BE:BE', 40)
            ws_acc.set_column('BF:BF', 40)
            ws_acc.set_column('BG:BG', 40)
            ws_acc.set_column('BH:BH', 40)
            ws_acc.set_column('BI:BI', 30)
            ws_acc.set_column('BJ:BJ', 30)
            ws_acc.set_column('BK:BK', 30)
            ws_acc.set_column('BL:BL', 30)
            ws_acc.set_column('BM:BM', 30)
            ws_acc.set_column('BN:BN', 30)
            ws_acc.set_column('BO:BO', 30)
            ws_acc.set_column('BP:BP', 30)
            ws_acc.set_column('BQ:BQ', 30)

            ws_acc.write('A2', "NO", format)
            ws_acc.write('B2', "NO. EVENT", format)
            ws_acc.write('C2', "NO. APKT", format)
            ws_acc.write('D2', "TANGGAL PADAM", format)
            ws_acc.write('E2', "LBS MANUAL / FCO", format)
            ws_acc.write('F2', "MTRZ", format)
            ws_acc.write('G2', "RECLOSER", format)
            ws_acc.write('H2', "PENYULANG GH", format)
            ws_acc.write('I2', "GARDU HUBUNG", format)
            ws_acc.write('J2', "PENYULANG GI", format)
            ws_acc.write('K2', "GARDU INDUK", format)
            ws_acc.write('L2', "JAM BUKA", format)
            ws_acc.write('M2', "JAM TRIP", format)
            ws_acc.write('N2', "JAM TUTUP", format)
            ws_acc.write('O2', "BEBAN PADAM", format)
            ws_acc.write('P2', "INDIKASI", format)
            ws_acc.write('Q2', "R", format)
            ws_acc.write('R2', "S", format)
            ws_acc.write('S2', "T", format)
            ws_acc.write('T2', "N", format)
            ws_acc.write('U2', "CUACA", format)
            ws_acc.write('V2', "ZONA TERGANGGU", format)
            ws_acc.write('W2', "UP3", format)
            ws_acc.write('X2', "ULP", format)
            ws_acc.write('Y2', "WILAYAH PADAM", format)
            ws_acc.write('Z2', "JUMLAH GARDU PADAM", format)
            ws_acc.write('AA2', "KATEGORI GANGGUAN", format)
            ws_acc.write('AB2', "PENYEBAB GANGGUAN", format)
            ws_acc.write('AC2', "GANGGUAN DITEMUKAN", format)
            ws_acc.write('AD2', "KETERANGAN", format)
            ws_acc.write('AE2', "JENIS PEMELIHARAAN", format)
            ws_acc.write('AF2', "PERALATAN RC", format)
            ws_acc.write('AG2', "RC OPEN", format)
            ws_acc.write('AH2', "RC CLOSE", format)
            ws_acc.write('AI2', "STATUS OPEN", format)
            ws_acc.write('AJ2', "STATUS CLOSE", format)
            ws_acc.write('AK2', "KOORDINASI PROTEKSI", format)
            ws_acc.write('AL2', "KETERANGAN", format)
            ws_acc.write('AM2', "SIMPATETIK TRIP", format)
            ws_acc.write('AN2', "GAGAL AR", format)
            ws_acc.write('AO2', "FAI ARUS GANGGUAN HMI", format)
            ws_acc.write('AP2', "PENYULANG FDIR", format)
            ws_acc.write('AQ2', "STATUS PENYULANG FDIR", format)
            ws_acc.write('AR2', "KETERANGAN FDIR", format)
            ws_acc.write('AS2', "FAI MTRZ HMI", format)
            ws_acc.write('AT2', "STATUS MTRZ HMI", format)
            ws_acc.write('AU2', "FAI FIOHL HMI", format)
            ws_acc.write('AV2', "STATUS FAI FIOHL HMI", format)
            ws_acc.write('AW2', "FAULT INDIKATOR KERJA", format)
            ws_acc.write('AX2', "SECTIONALYZER KERJA", format)
            ws_acc.write('AY2', "ACO KERJA", format)
            ws_acc.write('AZ2', "JAM WRC", format)
            ws_acc.write('BA2', "JAM ISOLASI", format)
            ws_acc.write('BB2', "JAM PENGUSUTAN", format)
            ws_acc.write('BC2', "JAM NORMAL", format)
            ws_acc.write('BD2', "DISPATCHER DCC KALSEL 1", format)
            ws_acc.write('BE2', "DISPATCHER DCC KALSEL 2", format)
            ws_acc.write('BF2', "DISPATCHER DCC KALSEL 3", format)
            ws_acc.write('BG2', "DISPATCHER DCC KALTENG 1", format)
            ws_acc.write('BH2', "DISPATCHER DCC KALTENG 2", format)
            ws_acc.write('BI2', "DISPATCHER DCC KALTENG 3", format)
            ws_acc.write('BJ2', "DURASI (MENIT)", format)
            ws_acc.write('BK2', "ENS (kWh)", format)
            ws_acc.write('BL2', "ENS (Rupiah)", format)
            ws_acc.write('BM2', "Durasi WRC", format)
            ws_acc.write('BN2', "Durasi Isolasi", format)
            ws_acc.write('BO2', "Durasi Pengusutan", format)
            ws_acc.write('BP2', "Durasi Perbaikan", format)
            ws_acc.write('BQ2', "Durasi Penormalan", format) 

            index = 1
            # for data in serializer.data:
            #     print(data['id_ref_lokasi'])
            #     # status = data['status_listrik']
            #     # if status == '0':
            #     #     status = 'inactive'
            #     # elif status == '1':
            #     #     status = 'active'
            #     # if data.get('up2b'):
            #     #     up2b = data.get('up2b', {}).get('nama_lokasi')
            #     # else:
            #     #     up2b = '' 

            #     # if data.get('parent_lokasi'):
            #     #     parent_lokasi = data.get('parent_lokasi', {}).get('id_ref_lokasi')
            #     #     name_parent_lokasi = data.get('parent_lokasi', {}).get('nama_lokasi')
            #     # else:
            #     #     parent_lokasi = ''
            #     #     name_parent_lokasi = ''

            #     ws_acc.write(index, 0, str(data['id_ref_lokasi']))
            #     ws_acc.write(index, 1, data['no_apkt'])
            #     ws_acc.write(index, 1, data['no_apkt'])
            #     ws_acc.write(index, 2, data['no_apkt'])
            #     ws_acc.write(index, 3, data['no_apkt'])
            #     ws_acc.write(index, 4, data['no_apkt'])
            #     ws_acc.write(index, 5, data['no_apkt'])
            #     ws_acc.write(index, 6, data['no_apkt'])
            #     ws_acc.write(index, 7, data['no_apkt'])
            #     ws_acc.write(index, 8, data['no_apkt'])
            #     ws_acc.write(index, 9, data['no_apkt'])
            #     ws_acc.write(index, 10, data['no_apkt'])
            #     index += 1
            workbook.close()
            response = HttpResponse(open(file_path, 'rb'), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(file_path)
            return response
        # except:
        #     return build_response(ApiResponse(message='files not found'))


    @extend_schema( 
        methods=["GET"],
        summary="Get Opsisdis - Rekap Padam - Trans Ep",
        description="Get Opsisdis - Rekap Padam - Trans Ep",
        parameters=[
            # OpenApiParameter(name='status', description='STATUS (Normal, Padam, Nyala Bertahap)', required=False, type=str, default=None),
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_rekap_padam']
    )
    def list(self, request):
        header = EXPORT_HEADERS
        relation = EXPORT_RELATION_FIELD
        header_caption = EXPORT_HEADERS_CAPTION
        export = request.GET['export'] if 'export' in request.GET else None
        export_type = request.GET['export_type'] if 'export_type' in request.GET else None  
        status = request.GET['status'] if 'status' in request.GET else '-'
        tanggal_after = request.GET['tanggal_after'] if 'tanggal_after' in request.GET else None
        tanggal_before = request.GET['tanggal_before'] if 'tanggal_before' in request.GET else None

        date_range = None
        if tanggal_after and tanggal_before:  
            date_range =  '%s' % (tanggal_after) + ' - ' + '%s' % (tanggal_before) 

        fields = EXPORT_FIELDS
        title = 'Laporan Rekap Padam - trans EP'
        queryset = self.filter_queryset(self.get_queryset())   
        if export and export_type:
            filter = {"status":status,"date_range":date_range,"export_type":export_type}
            # print(filter)
            return self.export(queryset=queryset,filter=filter)
        return get_response(self, request, queryset, 'trans_ep.view')  

        return get_response(self, request, queryset, 'trans_ep.view', headers=header, relation=relation,
                        fields=fields, title=title,header_caption=header_caption)  


    @extend_schema(
        methods=["POST"],
        summary="Create Opsisdis - Rekap Padam - Trans Ep",
        description="Create Opsisdis - Rekap Padam - Trans Ep",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['opsisdis_rekap_padam']
    ) 
    # create
    def create(self, request):
        data = request.data
        no_event = self.getNoEvent() 
        data['no_event'] = no_event  
        serializer = self.create_serializer_class(data=data) 
        return post_update_response(serializer, 'trans_ep.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Opsisdis - Rekap Padam - Trans Ep (Specified).",
        description="Get Opsisdis - Rekap Padam - Trans Ep (Specified).",
        tags=['opsisdis_rekap_padam']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        trans_ep = self.queryset.filter(id_trans_ep=pk)
        if not trans_ep:
            return not_found('trans_ep.not_found')

        serializer = self.serializer_class(trans_ep, many=True)
        return response__(request, serializer, 'trans_ep.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Opsisdis - Rekap Padam - Trans Ep",
        description="Update Opsisdis - Rekap Padam - Trans Ep",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['opsisdis_rekap_padam']
    )
    def update(self, request, pk):
        trans_ep = get_object_or_404(TransEp, pk=pk)
        if 'jam_normal' in request.data:
            # update ke jam tutup
            request.data['jam_tutup'] = request.data['jam_normal'] 
        serializer = self.update_serializer_class(instance=trans_ep, data=request.data)
        data_json = validate_serializer(serializer, s=True)   
        if data_json.get('error') == True: 
            return error_response(data_json.get('data'))  
        
        data_json = data_json.get('data')
        if 'jam_normal' in request.data or 'beban_padam' in request.data:
            id_trans_ep = pk 
            # cek trans_section normal dan last insert 
            data_ep = self.get_hitung_ens_serializer_class(trans_ep).data 
            if data_ep:
                trans_section = {
                    'id_trans_ep': id_trans_ep,
                    'jam_masuk' : request.data['jam_normal'],
                    'section' : 'normal', 
                    'id_user_entri' : request.data['id_user_update'],
                    'id_user_update' : request.data['id_user_update'],
                    'durasi' : data_ep.get('durasi'),
                    'ens' : data_ep.get('ens'),
                } 
                # exit()
                # get normal by id_trans_ep 
                # jika ada maka update normal 
                try:
                    trans_section_cek = TransEpSection.objects.get(id_trans_ep=id_trans_ep,section='normal')
                except TransEpSection.DoesNotExist:
                    trans_section_cek = None

                if trans_section_cek: 
                    _u = self.ep_section_update_serializer_class(instance=trans_section_cek, data=trans_section)  
                    if _u.is_valid(raise_exception=True):  
                        _u.save()
                        # print(_u.data) 
                else:
                    trans_section_i= {
                        'id_trans_ep': id_trans_ep,
                        'jam_masuk' : request.data['jam_normal'],
                        'section' : 'normal', 
                        'id_user_entri' : request.data['id_user_update'], 
                        'durasi' : data_ep.get('durasi'),
                        'ens' : data_ep.get('ens'),
                    }  
                    _i = self.ep_section_serializer_class(data=trans_section_i)
                    if _i.is_valid(raise_exception=False):  
                        _i.save()  
        return response_json(data = data_json, msg ='trans_ep.update')  

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Opsisdis - Rekap Padam - Trans Ep",
        description="Delete Opsisdis - Rekap Padam - Trans Ep",
        request=all_serializer_class,
        responses=all_serializer_class,
        tags=['opsisdis_rekap_padam']
    )
    def destroy(self, request, pk):
        trans_ep = get_object_or_404(TransEp, pk=pk)
        self.perform_destroy(trans_ep)
        return response__(request, trans_ep, 'trans_ep.delete')

    def perform_destroy(self, instance):
        instance.delete()
 
    
    @extend_schema(
        methods=["GET"],
        summary="Update Opsisdis - Rekap Padam - Trans Ep Get Peralatan Detail (Ref Lokasi)",
        description="Update Opsisdis - Rekap Padam - Trans Ep Get Peralatan Detail (Ref Lokasi)",
        request=get_peralatan_detail_serializer_class,
        responses=get_peralatan_detail_serializer_class,
        tags=['opsisdis_rekap_padam']
    )
    @action(detail=False, methods=['GET'], url_path='peralatan-detail/(?P<id_ref_lokasi>\d+)', url_name='get-peralatan-detail')
    def get_peralatan(self, request,id_ref_lokasi):
        trans_ep_peralatan = self.queryset_ref_lokasi.filter(id_ref_lokasi=id_ref_lokasi) 
        if not trans_ep_peralatan:
            return not_found('trans_ep.not_found')

        serializer = self.get_peralatan_detail_serializer_class(trans_ep_peralatan, many=True) 
        return response_retreve(queryset=serializer, msg='trans_ep.view_peralatan')

    # @extend_schema(
    #     methods=["GET"],
    #     summary="Update Opsisdis - Rekap Padam - Trans Ep Get Copy WA",
    #     description="Update Opsisdis - Rekap Padam - Trans Ep Get Copy WA",
    #     request=None,
    #     responses=None,
    #     tags=['opsisdis_rekap_padam']
    # )
    # @action(detail=False, methods=['GET'], url_path='copy-wa/(?P<id_trans_ep>\d+)', url_name='get-copy-wa')
    # def get_copy_wa(self, request,id_trans_ep):
    #     trans_ep = self.queryset.filter(id_trans_ep=id_trans_ep) 
    #     if not trans_ep:
    #         return not_found('trans_ep.not_found') 
    #     d = get_response_no_page(self, request=request, queryset=trans_ep) 
    #     # print(d[0].get('keypoint').get('gardu_induk').get('nama_lokasi') )

    #     padam_gangguan_arr = {
    #         "no_event": d[0].get('no_event'),
    #         "tanggal": d[0].get('tanggal'),
    #         "gardu_induk": d[0].get('keypoint').get('gardu_induk').get('nama_lokasi') if  d[0].get('keypoint').get('gardu_induk') else "-",
    #         "penyulang": d[0].get('keypoint').get('penyulang').get('nama_lokasi') if  d[0].get('keypoint').get('penyulang') else "-",
    #         "keypoint": d[0].get('keypoint').get('nama_lokasi') if  d[0].get('keypoint') else "-",
    #         "jenis_keypoint": d[0].get('jenis_keypoint'),
    #         "beban_padam": d[0].get('beban_padam'),
    #         "indikasi": d[0].get('ref_ep_indikasi').get('nama') if  d[0].get('ref_ep_indikasi') else "-",
    #         "r": d[0].get('r'),
    #         "s": d[0].get('s'),
    #         "t": d[0].get('t'),
    #         "n": d[0].get('n'),
    #         "fai": d[0].get('fai_arus_ggn_hmi'),
    #         "cuaca": d[0].get('ref_ep_cuaca').get('nama') if  d[0].get('keypoint') else "-",
    #         "up3": d[0].get('up3').get('nama_lokasi') if  d[0].get('up3') else "-",
    #         "ulp": d[0].get('ulp').get('nama_lokasi') if  d[0].get('ulp') else "-",
    #         "jlh_gardu_padam": d[0].get('jlh_gardu_padam'),
    #         "alamat": d[0].get('keypoint').get('alamat') if  d[0].get('keypoint') else "-",
    #         "ref_ep_penyebab_ggn": d[0].get('id_ref_ep_penyebab_ggn').get('nama') if  d[0].get('id_ref_ep_penyebab_ggn') else "-",
    #         "pelanggan_tm": d[0].get('pelanggan_tm'),
    #         "pelanggan_vip": d[0].get('pelanggan_vip'),
    #         "durasi_pengusutan": d[0].get('durasi_pengusutan'),
    #         "total_gangguan_month": d[0].get('total_gangguan_month'),
    #         "total_gangguan_year": d[0].get('total_gangguan_year'),
    #         "penanggung_jawab": '-',
    #         "pelaksana": '-',
    #         "pengawas_k3": '-',
    #         "pengawas_manuver": '-',
    #         "durasi_pekrjaan": '-',
    #         "estimasi_ens": '-',
    #         "durasi": d[0].get('durasi') if  d[0].get('durasi') else '-',
    #         "durasi_isolasi": d[0].get('durasi_isolasi') if  d[0].get('durasi_isolasi') else "-",
    #         "durasi_pengusutan": d[0].get('durasi_pengusutan') if  d[0].get('durasi_pengusutan') else "-",
    #         "durasi_perbaikan": d[0].get('durasi_perbaikan') if  d[0].get('durasi_perbaikan') else "-",
    #         "durasi_recovery": d[0].get('durasi_recovery') if  d[0].get('durasi_recovery') else "-",
    #         "ens": d[0].get('ens') if  d[0].get('ens') else "-",
    #         } 
    #     padam_gangguan_trip = "*INFORMASI GANGGUAN DCC KALSELTENG* <br> NO EVENT : %(no_event)s <br> Hari : %(tanggal)s <br> Gardu Induk : %(gardu_induk)s  <br> Penyulang GI : %(penyulang)s <br>Peralatan Trip : %(keypoint)s <br> Jenis Peralatan : %(jenis_keypoint)s <br> Beban Sebelum Trip :  %(beban_padam)s MW <br>Indikasi Gangguan : %(indikasi)s <br> Arus Gangguan : <br> R :  %(r)s A <br> S :   %(s)s A <br> T :  %(t)s A <br> N :  %(n)s A <br> AG BY :  %(fai)s <br> Cuaca :  %(cuaca)s <br> UP3 :  %(up3)s <br> ULP : %(ulp)s <br> Jumlah Gardu Padam : %(jlh_gardu_padam)s <br>Wilayah Padam :  %(alamat)s <br> Pelanggan Premium : %(pelanggan_tm)s <br> Pelanggan VIP :  %(pelanggan_vip)s <br> Kali GGN Selama Bulan :   %(total_gangguan_month)s Kali <br> Kali GGN Selama Tahun : %(total_gangguan_year)s Kali" % padam_gangguan_arr
    #     update_ggn = "*UPDATE PENGUSUTAN GANGGUAN DCC KALSELTENG*   <br> NO EVENT : %(no_event)s <br> Hari : %(tanggal)s <br> Gardu Induk : %(gardu_induk)s  <br> Penyulang GI : %(penyulang)s <br>Peralatan Trip : %(keypoint)s <br> Jenis Peralatan : %(jenis_keypoint)s <br> UP3 : %(up3)s <br> ULP : %(ulp)s <br> Status Pengusutan : %(durasi_pengusutan)s <br> Sisa Beban Padam : %(beban_padam)s <br> " % padam_gangguan_arr
    #     peromalan_ggn = "*UPDATE PENORMALAN GANGGUAN DCC KALSELTENG*   <br> NO EVENT : %(no_event)s <br> Hari : %(tanggal)s <br> Gardu Induk : %(gardu_induk)s  <br> Penyulang GI : %(penyulang)s <br>Peralatan Trip : %(keypoint)s <br> Jenis Peralatan : %(jenis_keypoint)s <br> UP3 : %(up3)s <br> ULP : %(ulp)s <br> Penyebab Gangguan : %(ref_ep_penyebab_ggn)s <br> Durasi Isolasi : %(durasi_isolasi)s Menit <br> Durasi Pengusutan  : %(durasi_pengusutan)s Menit <br> Durasi Perbaikan   : %(durasi_perbaikan)s Menit <br> Durasi Recovery    : %(durasi_recovery)s Menit <br> ENS    : %(ens)s kWh <br> ENS Dalam Rupiah   : %(ens)s kWh <br>" % padam_gangguan_arr
    #     pdm_emergency = "*INFORMASI PEKERJAAN/EMERGENCY DCC KALSELTENG*   <br> NO EVENT : %(no_event)s <br> Hari : %(tanggal)s <br> Gardu Induk : %(gardu_induk)s  <br> Penyulang GI : %(penyulang)s <br>Peralatan Trip : %(keypoint)s <br> Jenis Peralatan : %(jenis_keypoint)s <br> UP3 : %(up3)s <br> ULP : %(ulp)s Jumlah Gardu Padam : %(jlh_gardu_padam)s <br>Wilayah Padam :  %(alamat)s <br> Pelanggan Premium : %(pelanggan_tm)s <br> Pelanggan VIP :  %(pelanggan_vip)s <br> Penanggung Jawab :  %(penanggung_jawab)s <br> Pelaksana :  %(pelaksana)s <br> Pengawas K3 :  %(pengawas_k3)s <br> Pengawas Manuver :  %(pengawas_manuver)s <br> Durasi Pekerjaan :  %(durasi)s <br> Estimasi ENS :  %(estimasi_ens)s <br>" % padam_gangguan_arr
    #     update_terencana = "*UPDATE PEKERJAAN/EMERGENCY DCC KALSELTENG*   <br> NO EVENT : %(no_event)s <br> Hari : %(tanggal)s <br> Gardu Induk : %(gardu_induk)s  <br> Penyulang GI : %(penyulang)s <br>Peralatan Trip : %(keypoint)s <br> Jenis Peralatan : %(jenis_keypoint)s <br> UP3 : %(up3)s <br> ULP : %(ulp)s <br> Status Pengusutan : %(durasi_pengusutan)s <br> Sisa Beban Padam : %(beban_padam)s <br> " % padam_gangguan_arr
    #     permohonan_terencana = "*UPDATE PENORMALAN PEKERJAAN/EMERGENCY DCC KALSELTENG*   <br> NO EVENT : %(no_event)s <br> Hari : %(tanggal)s <br> Gardu Induk : %(gardu_induk)s  <br> Penyulang GI : %(penyulang)s <br>Peralatan Trip : %(keypoint)s <br> Jenis Peralatan : %(jenis_keypoint)s <br> UP3 : %(up3)s <br> ULP : %(ulp)s <br> Keterangan Pekerjaan : %(durasi_pengusutan)s <br> Durasi Pekerjaan : %(durasi)s <br> ENS    : %(ens)s kWh <br> ENS Dalam Rupiah   : %(ens)s kWh <br>" % padam_gangguan_arr
    #     data =[{
    #         'padam_gangguan_trip':padam_gangguan_trip,
    #         'update_ggn':update_ggn,
    #         'peromalan_ggn':peromalan_ggn,
    #         'pdm_emergency':pdm_emergency,
    #         'update_terencana':update_terencana,
    #         'permohonan_terencana':permohonan_terencana,
    #         'data':padam_gangguan_arr,
    #     }]
    #     # print(padam_gangguan_trip) 
    #     return response_basic(_status=True, msg='trans_ep.view_wa',results=data)
    
 
    # @extend_schema(
    #     methods=["PUT"],
    #     summary="Update Opsisdis - Rekap Padam - Trans Ep Status Update",
    #     description="Update Opsisdis - Rekap Padam - Trans Ep Status Update",
    #     request=update_status_serializer_class,
    #     responses=update_status_serializer_class,
    #     tags=['opsisdis_rekap_padam']
    # )
    # @action(detail=False, methods=['PUT'], url_path='status/(?P<id_trans_ep>\d+)', url_name='update-status')
    # def update_status(self, request, id_trans_ep):
    #     trans_ep = get_object_or_404(TransEp, pk=id_trans_ep)
    #     serializer = self.update_status_serializer_class(instance=trans_ep, data=request.data)
    #     return post_update_response(serializer, 'trans_ep.update') 

class TransEpPeralatanViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefLokasi.objects.all() 
    serializer_class = serializers.PeralatanSerializers 

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = PeralatanFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama_lokasi']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_ref_lokasi']

    @extend_schema( 
        methods=["GET"],
        summary="Get Opsisdis - Rekap Padam - Trans Ep Peralatan (Ref Lokasi)",
        description="Get Opsisdis - Rekap Padam - Trans Ep Peralatan (Ref Lokasi)",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10), 
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_rekap_padam']
    )
    def list(self, request): 
        queryset = self.filter_queryset(self.get_queryset())   
 
        return get_response(self, request, queryset, 'trans_ep.view')  

    @extend_schema(
        methods=["GET"],
        summary="Update Opsisdis - Rekap Padam - FAI arus ggn HMI",
        description="Update Opsisdis - Rekap Padam - FAI arus ggn HMI",
        request=None,
        responses=None,
        tags=['opsisdis_rekap_padam']
    )
    @action(detail=False, methods=['GET'], url_path='fai-arus-ggn-hmi', url_name='fai-arus-ggn-hmi')
    def arus_ggn(self, request): 
        data = [
            {'name':'AG BY HMI'}, 
            {'name':'AG BY OPERATOR GI'}, 
            {'name':'AG BY UP3'}, 
            {'name':'AG TIDAK TERBACA'} 
        ]
        status_ = status.HTTP_200_OK

        raw_response = {
            "status": status_,
            "message": 'Berhasil mendapatkan ref FAI arus ggn HMI',
            "results": data
        }
        return response.Response(data=raw_response, status=status_)

class TransEpExportRCViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TransEpPeralatan.objects.all() 
    serializer_class = ExportTransEpPeralatanSerializers 

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TransEpPeralatanFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['rc_open','rc_close','status_rc_open','status_rc_close']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_ep_peralatan']

    @extend_schema( 
        methods=["GET"],
        summary="Get Opsisdis - Rekap Padam - Trans Ep Export RC",
        description="Get Opsisdis - Rekap Padam - Trans Ep Export RC",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_rekap_padam']
    )
    def list(self, request):
        
        header = EXPORT_HEADERS
        relation = EXPORT_RELATION_FIELD
        header_caption = EXPORT_HEADERS_CAPTION

        fields = EXPORT_FIELDS
        title = 'Rekap Perlatan RC'
        cl = dict()
        status = request.GET['status'] if 'status' in request.GET else None
        tanggal_after = request.GET['tanggal_after'] if 'tanggal_after' in request.GET else None
        tanggal_before = request.GET['tanggal_before'] if 'tanggal_before' in request.GET else None 
        if tanggal_after and tanggal_before:  
            custom_label =  '%s' % (tanggal_after) + ' - ' + '%s' % (tanggal_before)
            cl['date_range'] = custom_label
        else:
            cl['date_range'] = '-'

        if status:
            cl['status'] = status  
        else:
            cl['status'] = 'Semua'   
        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'trans_ep.view', headers=header, relation=relation,
                        fields=fields, title=title,header_caption=header_caption, custom_label=cl)    
    

    