from numpy import source
from rest_framework import filters
from django_filters import rest_framework

from .models import ScadaSOEModels


class ScadaSOEFilters(rest_framework.FilterSet): 
  
    class Meta:
        model = ScadaSOEModels
        fields = ['time_stamp', 'path1', 'path2', 'path3', 'path4','path5','elem','info','tag']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
