from numpy import source
from rest_framework import filters
from django_filters import rest_framework
from .models import TransTmPenyulangBulan


class TransTmPenyulangBulanFilter(rest_framework.FilterSet): 
    month = rest_framework.DateTimeFromToRangeFilter(field_name='datum',label='(yyyy-mm-dd)') 

    # month_after = rest_framework.DateFilter(field_name='datum__month',lookup_expr='lt', method='filter_month_after') 
    # month_before = rest_framework.DateFilter(field_name='datum__month',lookup_expr='gt', method='filter_month_before') 

    # def filter_month_after(self, queryset, name, value):  
    #     date =  value
    #     if date: 
    #         year = value.split('-')[0] 
    #         month = value.split('-')[1]  

    #     return queryset.filter(datum__year__gte=year ,datum__month__gte=month )
    # def filter_month_before(self, queryset, name, value):  
    #     date =  value
    #     if date: 
    #         year = value.split('-')[0] 
    #         month = value.split('-')[1]  
    #     return queryset.filter(datum__year__gte=year ,datum__month__gte=month )

    # datum_month = rest_framework.NumberFilter(field_name='datum__month', lookup_expr='exact')
    # datum_month = rest_framework.NumberFilter(field_name='datum', lookup_expr='month')
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
        model = TransTmPenyulangBulan
        fields = ['id_ref_lokasi_gi', 'id_ref_lokasi_trafo_gi','id_ref_lokasi_penyulang','datum']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
