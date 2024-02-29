from .models import ScadaSOEModels , EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS, EXPORT_HEADERS_CUSTOM_XLSX, EXPORT_HEADERS_CAPTION
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, response, status
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from .serializers import ScadaSOESerializer
from base.custom_pagination import CustomPagination
from .filters import ScadaSOEFilters, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from drf_spectacular.utils import extend_schema, OpenApiParameter
from base.response import response__, get_response, not_found, response_basic ,validate_serializer, error_response,response_json
from django_filters import rest_framework
from library.date_converter import date_converter_dt ,date_converter_str

from django.db.models import Q




# Create your views here.
class ScadaSOEViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]


    serializer_class = ScadaSOESerializer
    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = ScadaSOEFilters
    filterset_fields = ['keyword']   # multi filter param
    search_fields = ['path1', 'path2', 'path3', 'path4','path5','elem','info','tag']  # multi filter field
    ordering_fields = ['path1', 'path2', 'path3', 'path4','path5','elem','info','tag']
    # ordering = ['id']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Fasop - SCADA -  Message(SOE)",
        description="Get Data Fasop - SCADA -  Message(SOE)",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),


            OpenApiParameter(name='not_b1', description='Cekbox B1', required=False, type=bool, default=False),
            OpenApiParameter(name='op_b1', description='Operator B1 ', required=False, type=str),
            OpenApiParameter(name='b1', description='Path B1 ', required=False, type=str),
                             


            OpenApiParameter(name='not_b2', description='Cekbox B2', required=False, type=bool, default=False),
            OpenApiParameter(name='op_b2', description='Operator B2', required=False, type=str),
            OpenApiParameter(name='b2', description='Path B2', required=False, type=str),


            OpenApiParameter(name='not_b3', description='Cekbox B3', required=False, type=bool, default=False),
            OpenApiParameter(name='op_b3', description='Operator B3', required=False, type=str),
            OpenApiParameter(name='b3', description='Path B3', required=False, type=str),


            OpenApiParameter(name='not_element', description='Cekbox Element',required=False, type=bool, default=False),
            OpenApiParameter(name='op_element', description='Operator Element',required=False, type=str),
            OpenApiParameter(name='elem', description='Path Element',required=False, type=str),

            OpenApiParameter(name='not_info', description='Cekbox Info',required=False, type=bool, default=False),
            OpenApiParameter(name='op_info', description='Operator Info',required=False, type=str),
            OpenApiParameter(name='info', description='Path Info',required=False, type=str),


            OpenApiParameter(name='not_tag', description='Cekbox Label',required=False, type=bool, default=False),
            OpenApiParameter(name='op_tag', description='Operator Label',required=False, type=str),
            OpenApiParameter(name='tag', description='Path Label',required=False, type=str),
            
            
            OpenApiParameter(name='time_stamp_start', description='Tanggal Mulai Contoh : 2022-05-11',required=False, type=str),
            OpenApiParameter(name='time_stamp_end', description='Tanggal Akhir Contoh : 2022-05-11',required=False, type=str),



        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['laporan_scada']
    )
    def list(self, request, *args, **kwargs):
        
        header = EXPORT_HEADERS
        relation = EXPORT_RELATION_FIELD
        header_custom = EXPORT_HEADERS_CUSTOM_XLSX
        header_caption = EXPORT_HEADERS_CAPTION
        fields = EXPORT_FIELDS
        title = 'Scada Message(SOE)'

        time_stamp_start =  request.GET.get('time_stamp_start', None)
        time_stamp_end =  request.GET.get('time_stamp_end', None)
        b1 =  request.GET.get('b1', None)
        opb1 =  request.GET.get('op_b1', None)
        notb1 =  request.GET.get('not_b1', None)

        b2 =  request.GET.get('b2', None)
        opb2 =  request.GET.get('op_b2', None)
        notb2 =  request.GET.get('not_b2', None)

        b3 =  request.GET.get('b3', None)
        opb3 =  request.GET.get('op_b3', None)
        notb3 =  request.GET.get('not_b3', None)

        elem =  request.GET.get('elem', None)
        opelement =  request.GET.get('op_element', None)
        notelement =  request.GET.get('not_element', None)

        info =  request.GET.get('info', None)
        opinfo =  request.GET.get('op_info', None)
        notinfo =  request.GET.get('not_info', None)

        tag =  request.GET.get('tag', None)
        optag =  request.GET.get('op_tag', None)
        notag =  request.GET.get('not_tag', None)

        time_stamp_start = date_converter_dt(date=time_stamp_start,time='00:00:00')
        time_stamp_end = date_converter_dt(date=time_stamp_end,time='23:59:00')   


        keyword = request.GET.get('keyword')

        queryset = self.filter_queryset(ScadaSOEModels.objects.all())

        if b1:
            if notb1:
                if opb1 == 'and':
                    queryset = self.filter_queryset(ScadaSOEModels.objects.filter(time_stamp__range=(time_stamp_start,time_stamp_end) & ~Q(path1__contains=b1.upper())))
                elif opb1 == 'or':
                    queryset = self.filter_queryset(ScadaSOEModels.objects.filter(time_stamp__range=(time_stamp_start,time_stamp_end) | ~Q(path1__contains=b1.upper())))
            else:
                queryset = self.filter_queryset(ScadaSOEModels.objects.filter(Q(time_stamp__range=(time_stamp_start,time_stamp_end)) & Q(path1__contains=b1.upper())))


        if b2:
            if notb2:
                if opb2 == 'and':
                    queryset = self.filter_queryset(ScadaSOEModels.objects.filter(time_stamp__range=(time_stamp_start,time_stamp_end) & ~Q(path2__contains=b2.upper())))
                elif opb2 == 'or':
                    queryset = self.filter_queryset(ScadaSOEModels.objects.filter(time_stamp__range=(time_stamp_start,time_stamp_end) | ~Q(path2__contains=b2.upper())))
            else:
                queryset = self.filter_queryset(ScadaSOEModels.objects.filter(Q(time_stamp__range=(time_stamp_start,time_stamp_end)) & Q(path2__contains=b2.upper())))

        if b3:
            if notb3:
                if opb3 == 'and':
                    queryset = self.filter_queryset(ScadaSOEModels.objects.filter(time_stamp__range=(time_stamp_start,time_stamp_end) & ~Q(path3__contains=b3.upper())))
                elif opb3 == 'or':
                    queryset = self.filter_queryset(ScadaSOEModels.objects.filter(time_stamp__range=(time_stamp_start,time_stamp_end) | ~Q(path3__contains=b3.upper())))
            else:
                queryset = self.filter_queryset(ScadaSOEModels.objects.filter(Q(time_stamp__range=(time_stamp_start,time_stamp_end)) & Q(path3__contains=b3.upper())))
        
        if elem:
            if notelement:
                if opelement == 'and':
                    queryset = self.filter_queryset(ScadaSOEModels.objects.filter(time_stamp__range=(time_stamp_start,time_stamp_end) & ~Q(path4__contains=elem.upper())))
                elif opelement == 'or':
                    queryset = self.filter_queryset(ScadaSOEModels.objects.filter(time_stamp__range=(time_stamp_start,time_stamp_end) | ~Q(path4__contains=elem.upper())))
            else:
                queryset = self.filter_queryset(ScadaSOEModels.objects.filter(Q(time_stamp__range=(time_stamp_start,time_stamp_end)) & Q(path4__contains=elem.upper())))

        if info:
            if notinfo:
                if opinfo == 'and':
                    queryset = self.filter_queryset(ScadaSOEModels.objects.filter(time_stamp__range=(time_stamp_start,time_stamp_end) & ~Q(path5__contains=info.upper())))
                elif opinfo == 'or':
                    queryset = self.filter_queryset(ScadaSOEModels.objects.filter(time_stamp__range=(time_stamp_start,time_stamp_end) | ~Q(path5__contains=info.upper())))
            else:
                queryset = self.filter_queryset(ScadaSOEModels.objects.filter(Q(time_stamp__range=(time_stamp_start,time_stamp_end)) & Q(path5__contains=info.upper())))
        
        if tag:
            if notag:
                if optag == 'and':
                    queryset = self.filter_queryset(ScadaSOEModels.objects.filter(time_stamp__range=(time_stamp_start,time_stamp_end) & ~Q(msgstatus__contains=tag.upper())))
                elif optag == 'or':
                    queryset = self.filter_queryset(ScadaSOEModels.objects.filter(time_stamp__range=(time_stamp_start,time_stamp_end) | ~Q(msgstatus__contains=tag.upper())))
            else:
                queryset = self.filter_queryset(ScadaSOEModels.objects.filter(Q(time_stamp__range=(time_stamp_start,time_stamp_end)) & Q(msgstatus__contains=tag.upper())))

   
        return get_response(self, request, queryset, 'sch_his_message.view',headers=header, relation=relation, fields=fields,title=title, header_custom=header_custom, )

    
       
