from numpy import source
from rest_framework import filters
from django_filters import rest_framework
from .models import SCD_MASTER_RTL


class SCD_MASTER_RTLFilter(rest_framework.FilterSet):
    datum = rest_framework.DateTimeFromToRangeFilter(field_name='datum',label='datum(24hour) example: (2022-05-11 13:00) bisa milisecond') 
    datum_1 = rest_framework.DateTimeFromToRangeFilter(field_name='datum_1',label='datum_1(24hour) example: (2022-05-11 13:00) bisa milisecond') 
    datum_2 = rest_framework.DateTimeFromToRangeFilter(field_name='datum_2',label='datum_2(24hour) example: (2022-05-11 13:00) bisa milisecond')
    path3text = rest_framework.CharFilter(field_name='path3text', method='filter_path3text') 
    path3 = rest_framework.CharFilter(field_name='path3', method='filter_path3') 

    def filter_path3text(self, queryset, name, value):  
        return queryset.filter(point_number__path1text__contains=value)

    def filter_path3(self, queryset, name, value):  
        return queryset.filter(point_number__path1text__contains=value)
 
    class Meta:
        model = SCD_MASTER_RTL
        fields = ['status', 'status_1', 'status_2', 'datum','datum_1','datum_2','point_number','kesimpulan']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
