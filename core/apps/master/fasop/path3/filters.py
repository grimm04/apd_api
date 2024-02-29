from rest_framework import filters
from django_filters import rest_framework
from .models import FASOPPATH3

class FASOPPATH3Filter(rest_framework.FilterSet):

    class Meta:
        model = FASOPPATH3
        fields = ['path1','path2','path3','id_lokasi']

class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
