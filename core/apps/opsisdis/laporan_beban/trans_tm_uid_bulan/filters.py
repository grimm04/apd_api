from numpy import source
from rest_framework import filters
from django_filters import rest_framework
from .models import TransTmUidBulan


class TransTmUidBulanFilter(rest_framework.FilterSet):  
    month = rest_framework.DateTimeFromToRangeFilter(field_name='datum',label='(yyyy-mm-dd)')  
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
    pemilik = rest_framework.CharFilter(method='filter_pemilik', label='Pemilik') 

    def filter_pemilik(self, queryset, name, value):
        return queryset.filter(id_ref_lokasi_uid__pemilik__exact=value)
    class Meta:
        model = TransTmUidBulan
        fields = ['id_ref_lokasi_uid', 'datum']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
