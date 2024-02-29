from rest_framework import filters
from django_filters import rest_framework
from apps.master.fasop.point_type.models import PointType
from apps.master.fasop.rtu.models import RTU
from apps.master.fasop.c_point.models import CPoint
def filters_childs(serializer= None,context=None, queryset =None,filters= None, filter_q=None, jenispoint=None):
    qs = queryset    

    #check if context params is not null
    if 'query_params' not in context:  
        return serializer(qs, many=True, read_only=True, context={'query_params':context,'jenispoint':jenispoint}).data 

    context = context['query_params']
    query_params = context.copy() 
    
    
    #spit query params get __params
    params = {k.split('__', 1)[1]: v
               for k, v in query_params.items() if k.startswith(filter_q)} 
    # print(params)
    mqs = filters(params, queryset=qs).qs.distinct() 
    # if 'sort_by' in context: 
    #     sq = context['sort_by'].split(',') 
    #     #example desc child_pointtype__-no_urut,child_pointtype__-name,-no_urut
    #     sort_by = [k.split('__', 1)[1] for k in sq if k.startswith(filter_q)]  
    #     sort_by = ", ".join(repr(e) for e in sort_by)
    #     print(type(sort_by))
    #     mqs = mqs.order_by(int(sort_by))
    return serializer(mqs, many=True, read_only=True, context={'query_params':context,'jenispoint':jenispoint}).data  


class ChildPointtypeFilter(rest_framework.FilterSet):
    class Meta:
        model = PointType
        fields = ['status']

class RTUMasterypeFilter(rest_framework.FilterSet):
    class Meta:
        model = RTU
        fields = ['status']


class CPointFilter(rest_framework.FilterSet):
    # path4 = CharInFilter(field_name='path4', lookup_expr='in')

    class Meta:
        model = CPoint
        # fields = ['id_pointtype', 'point_name', 'point_type', 'active', 'aor_id', 'aor_id_dw', 'int',
        #           'tariff_group_id', 'ctrl_area_int_id', 'ctrl_area_ext_id', 'meas_unit', 'state_set_id',
        #           'collection_rate', 'absolute_error', 'significant_digits', 'energy_type',
        #           'import_export', 'counter_type', 'scaling_facktor', 'rollover_limit', 'precision_processing',
        #           'created', 'ddc_trigger_report_flag', 'system_id', 'collection_delay', 'value',
        #           'last_update', 'p1', 'p2', 'p3', 'p4', 'p5', 'element', 'info', 'status_network', 'update_network',
        #           'kinerja', 'id_station', 'point_class', 'send_telegram', 'elementtext', 'capture_telemetring',
        #           'format_pesan', 'durasi_perubahan', 'rc', 'trip', 'rc_telegram', 'trip_telegram',
        #           'status', 'wilayah']
        fields = ['point_number', 'path1', 'path2', 'path3', 'path5', 'id_pointtype', 'point_type',
                  'kinerja', 'capture_telemetring', 'active']
         
class CharInFilter(rest_framework.BaseInFilter, rest_framework.CharFilter):
    pass


class PointTypeFilter(rest_framework.FilterSet):
    jenispoint = CharInFilter(field_name='jenispoint', lookup_expr='in')
    # status_child = rest_framework.CharFilter(field_name='status_child', method='filter_status_child',label='status_child')  

    # def filter_status_child(self, queryset, name, value):  
    #     return queryset.select_related('id_induk_pointtype').filter(id_induk_pointtype__status__contains=value)
    class Meta:
        model = PointType
        fields = ['status', 'datum_created', 'log_his', 'show_grafik', 'no_urut', 'warna', 'send_telegram',
                  'format_pesan', 'durasi_perubahan',  ]


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
