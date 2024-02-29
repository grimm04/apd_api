from numpy import source
from rest_framework import filters
from django_filters import rest_framework
from .models import WP_PERTANYAAN_QRC


class WP_PERTANYAAN_QRCFilter(rest_framework.FilterSet): 
    class Meta:
        model = WP_PERTANYAAN_QRC
        fields = ['point']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
