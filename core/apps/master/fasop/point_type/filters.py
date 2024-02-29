from rest_framework import filters
from django_filters import rest_framework
from .models import PointType


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
                  'format_pesan', 'durasi_perubahan']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
