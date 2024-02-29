from numpy import source
from rest_framework import filters
from django_filters import rest_framework
from .models import WP_TTD_ONLINE


class WP_TTD_ONLINEFilter(rest_framework.FilterSet): 
    class Meta:
        model = WP_TTD_ONLINE
        fields = ['id_user','nama','nama_file','group_file','id_user_entri','id_user_update']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
