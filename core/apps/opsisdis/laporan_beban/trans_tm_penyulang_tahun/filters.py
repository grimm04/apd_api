from numpy import source
from rest_framework import filters
from django_filters import rest_framework
from .models import TransTmPenyulangTahun


class TransTmPenyulangTahunFilter(rest_framework.FilterSet):
    year = rest_framework.DateTimeFromToRangeFilter(field_name='datum',label='(yyyy-mm-dd)') 
    # datum_1 = rest_framework.DateTimeFromToRangeFilter(field_name='datum_1',label='datum_1(24hour) example: (2022-05-11 13:00) bisa milisecond') 
    # datum_2 = rest_framework.DateTimeFromToRangeFilter(field_name='datum_2',label='datum_2(24hour) example: (2022-05-11 13:00) bisa milisecond') 
    # path1 = rest_framework.CharFilter(field_name='path1', method='filter_path1')
    # id_pointtype = rest_framework.NumberFilter(field_name='id_pointtype', method='filter_id_pointtype') 

    # def filter_path1(self, queryset, name, value):  
    #     return queryset.filter(point_number__path1__contains=value)

    # def filter_id_pointtype(self, queryset, name, value):  
    #     return queryset.filter(point_number__id_pointtype=value)
    # datum_year = rest_framework.NumberFilter(field_name='datum', lookup_expr='year')
    i_max_siang_gte = rest_framework.CharFilter(field_name='i_max_siang', lookup_expr='gte' ,label="Ampere >=")
    i_max_siang_lte = rest_framework.CharFilter(field_name='i_max_siang', lookup_expr='lte', label="Ampere <=")
    i_max_siang_exact = rest_framework.CharFilter(field_name='i_max_siang', lookup_expr='exact', label="Ampere =")
    p_max_siang_gte = rest_framework.CharFilter(field_name='p_max_siang', lookup_expr='gte' ,label="MW >=")
    p_max_siang_lte = rest_framework.CharFilter(field_name='p_max_siang', lookup_expr='lte', label="MW <=")
    p_max_siang_exact = rest_framework.CharFilter(field_name='p_max_siang', lookup_expr='exact', label="MW =")
    i_max_malam_gte = rest_framework.CharFilter(field_name='i_max_malam', lookup_expr='gte' ,label="Ampere >=")
    i_max_malam_lte = rest_framework.CharFilter(field_name='i_max_malam', lookup_expr='lte', label="Ampere <=")
    i_max_malam_exact = rest_framework.CharFilter(field_name='i_max_malam', lookup_expr='exact', label="Ampere =")
    p_max_malam_gte = rest_framework.CharFilter(field_name='p_max_malam', lookup_expr='gte' ,label="MW >=")
    p_max_malam_lte = rest_framework.CharFilter(field_name='p_max_malam', lookup_expr='lte', label="MW <=")
    p_max_malam_exact = rest_framework.CharFilter(field_name='p_max_malam', lookup_expr='exact', label="MW =")
    class Meta:
        model = TransTmPenyulangTahun
        fields = ['id_ref_lokasi_gi', 'id_ref_lokasi_trafo_gi','id_ref_lokasi_penyulang','datum']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
