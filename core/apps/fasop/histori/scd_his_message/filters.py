from numpy import source
from rest_framework import filters
from django_filters import rest_framework
from .models import SCD_HIS_MESSAGE


class SCD_HIS_MESSAGEFilter(rest_framework.FilterSet): 
    time_stamp = rest_framework.DateTimeFromToRangeFilter(field_name='time_stamp',label='time_stamp(24hour) example: (2022-05-11 13:00)')  
    
    class Meta:
        model = SCD_HIS_MESSAGE
        fields = ['path1', 'path2', 'path3', 'path4','path5','elem','info','tag']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
