from numpy import source
from rest_framework import filters
from django_filters import rest_framework
from .models import SCD_KIN_DIGITAL_BULAN


class SCD_KIN_DIGITAL_BULANFilter(rest_framework.FilterSet):
    datum = rest_framework.DateFromToRangeFilter(field_name='datum',label='datum(24hour) example: (2022-01-01)')   
    path1 = rest_framework.CharFilter(field_name='path1', method='filter_path1')
    path3 = rest_framework.CharFilter(field_name='path3', method='filter_path3')
    id_pointtype = rest_framework.NumberFilter(field_name='id_pointtype', method='filter_id_pointtype') 

    def filter_path1(self, queryset, name, value):  
        return queryset.filter(point_number__path1__contains=value)

    def filter_path3(self, queryset, name, value):  
        return queryset.filter(point_number__path3__contains=value)

    def filter_id_pointtype(self, queryset, name, value):  
        return queryset.filter(point_number__id_pointtype=value)
    class Meta:
        model = SCD_KIN_DIGITAL_BULAN
        fields = ['datum']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
