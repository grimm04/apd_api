from numpy import source
from rest_framework import filters
from django_filters import rest_framework
from .models import SCD_HIS_RC


class SCD_HIS_RCFilter(rest_framework.FilterSet):
    datum_1 = rest_framework.DateTimeFromToRangeFilter(field_name='datum_1',label='datum_1(24hour) example: (2022-05-11 13:00)')  
    class Meta:
        model = SCD_HIS_RC
        fields = ['path1', 'path2', 'path3','b1','b2','b3','status_1','status_2','elem']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
