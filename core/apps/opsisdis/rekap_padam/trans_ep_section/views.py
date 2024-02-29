from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import TransEpSection
from .filters import TransEpSectionFilter, SearchFilter, TransEpSection
from apps.opsisdis.rekap_padam.trans_ep.models import TransEp
from apps.opsisdis.rekap_padam.trans_ep.serializers import AllNorelationTransEpSerializers
from base.response import response__, get_response, post_update_response, validate_serializer,error_response,response_json
from base.custom_pagination import CustomPagination 

class TransEpSectionViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TransEpSection.objects.all()
    serializer_class = serializers.TransEpSectionSerializers 
    create_serializer_class = serializers.CRTransEpSectionSerializers 
    update_serializer_class = serializers.UDTransEpSectionSerializers 
    ep_serializer_class =   serializers.GetTransEpSerializers
    ep_single_serializer_class =   serializers.GetTransSignleEpSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TransEpSectionFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['section','beban_masuk','durasi']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_ep_section']

    @extend_schema(
        methods=["GET"],
        summary="Get Opsisdis - Rekap Padam - Trans Ep Section",
        description="Get Opsisdis - Rekap Padam - Trans Ep Section",
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

        return get_response(self, request, queryset, 'trans_ep_section.view')


    @extend_schema(
        methods=["POST"],
        summary="Create Opsisdis - Rekap Padam - Trans Ep Section",
        description="Create Opsisdis - Rekap Padam - Trans Ep Section",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['opsisdis_rekap_padam']
    )
    # create
    def create(self, request):
        data = request.data
        # serializer = self.create_serializer_class(data=data)
        s2 = self.create_serializer_class(data=data)
        beban_masuk = request.data['beban_masuk'] 
        if s2.is_valid(raise_exception=False): 
            # serializer.save() 
            jam_masuk = data['jam_masuk']
            id_user_entri = data['id_user_entri']
            id_trans_ep = request.data['id_trans_ep']

            # get data Trans Ep by id
            trans_ep = TransEp.objects.get(id_trans_ep=id_trans_ep)
            data_ep = self.ep_serializer_class(trans_ep).data  
            # print(data_ep)
            beban_padam = data_ep.get('beban_padam')
            jam_padam = data_ep.get('jam_padam')
            cek_last_section = TransEpSection.objects.filter(id_trans_ep=id_trans_ep).values().order_by('-id_trans_ep_section')[0]
            if cek_last_section.get('section') != 'normal':
                if cek_last_section: 
                    beban_padam = cek_last_section.get('beban_masuk')
                else:
                    beban_padam = data_ep.get('beban_padam') 
                #jika sisa beban/beban masuk lebih besar(beban Normal) 
                if float(beban_masuk) >= float(beban_padam):
                    trans_section_normal = {
                        'id_trans_ep': id_trans_ep,
                        'jam_masuk' : jam_masuk,
                        'section' : 'normal', 
                        'id_user_entri' : id_user_entri, 
                        'durasi' : data_ep.get('durasi'),
                        'ens' : data_ep.get('ens'),
                    } 
                    # print(trans_section_normal)
                    beban_normal = self.create_serializer_class(data=trans_section_normal)
                    if beban_normal.is_valid(raise_exception=False):  
                        beban_normal.save() 
                        # update jam_tutup trans ep
                        trans_ep = TransEp.objects.filter(id_trans_ep=id_trans_ep) 
                        trans_ep.update(jam_normal=jam_masuk) 
                    return response_json(data = beban_normal.data, msg ='trans_ep_section.create')   
                else:  
                    trans_ep_section_cek = TransEpSection.objects.filter(id_trans_ep=id_trans_ep)
                    # jika tidak ada section by id trans ep 
                    if not trans_ep_section_cek: 
                        section = data_ep.get('keypoint_name')
                        durasi = data_ep.get('durasi')
                        ens = data_ep.get('ens') 
                        trans_section_1 = {
                            'id_trans_ep': id_trans_ep,
                            'jam_masuk' : jam_masuk,
                            'section' : section,
                            'beban_masuk' : beban_padam,
                            # 'beban_sebelum' : beban_padam,
                            # 'jam_sebelum' : jam_padam,
                            'id_user_entri' : id_user_entri,
                            'durasi' : durasi,
                            'ens' : ens,
                        }
                        # print(trans_section_1) 
                        s1 = self.create_serializer_class(data=trans_section_1)
                        if s1.is_valid(raise_exception=False):  
                            s1.save()
                            # update jam_tutup trans ep
                            trans_ep = TransEp.objects.filter(id_trans_ep=id_trans_ep) 
                            trans_ep.update(jam_tutup=jam_masuk) 
                            section_1 = s1.data
                            if section_1:
                                s2.save()      
                    else :   
                        durasi = data_ep.get('durasi')
                        ens = data_ep.get('ens')
                        # update data last section by id ep
                        _uls = { 
                            'id_trans_ep' : id_trans_ep,
                            'id_user_update' : id_user_entri,
                            'durasi' : durasi,
                            'ens' : ens,
                        }
                        print(_uls)
                        trans_ep_section_update = TransEpSection.objects.filter(id_trans_ep=id_trans_ep).order_by('-id_trans_ep_section')[0]
                        # print(trans_ep_section_update) 
                        #insert data section
                        _ulast = self.update_serializer_class(instance=trans_ep_section_update, data=_uls) 
                        if _ulast.is_valid(raise_exception=True):  
                            _ulast.save() 
                            #simpan data section terahkir di inputkan
                            s2.save()    
            return response_json(data = None, msg ='trans_ep_section.cant_add')   
        return response_json(data = s2.data, msg ='trans_ep_section.create')  
        
        # return post_update_response(serializer, 'trans_ep_section.create')

    # @extend_schema(
    #     methods=["GET"],
    #     summary="Get Opsisdis - Rekap Padam - Trans Ep Section (Specified).",
    #     description="Get Opsisdis - Rekap Padam - Trans Ep Section (Specified).",
    #     tags=['opsisdis_rekap_padam']
    # )
    # def retrieve(self, request, pk, *args, **kwargs):
    #     trans_ep_section = self.queryset.filter(id_trans_ep_section=pk)
    #     if not trans_ep_section:
    #         return not_found('trans_ep_section.not_found')

    #     serializer = self.serializer_class(trans_ep_section, many=True)
    #     return response__(request, serializer, 'trans_ep_section.view')
    
    # @extend_schema(
    #     methods=["PUT"],
    #     summary="Update Opsisdis - Opsisdis -  Trans Ep Section",
    #     description="Update Opsisdis - Opsisdis -  Trans Ep Section",
    #     request=serializer_class,
    #     responses=serializer_class,
    #     tags=['opsisdis_rekap_padam']
    # )
    # def update(self, request, pk):
    #     trans_ep_section = get_object_or_404(TransEpSection, pk=pk)
    #     serializer = self.serializer_class(instance=trans_ep_section, data=request.data)

    #     return post_update_response(serializer, 'trans_ep_section.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Opsisdis - Rekap Padam - Trans Ep Section",
        description="Delete Opsisdis - Rekap Padam - Trans Ep Section",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_rekap_padam']
    )
    def destroy(self, request, pk):
        trans_ep_section = get_object_or_404(TransEpSection, pk=pk)
        self.perform_destroy(trans_ep_section)
        return response__(request, trans_ep_section, 'trans_ep_section.delete')

    def perform_destroy(self, instance):
        instance.delete()