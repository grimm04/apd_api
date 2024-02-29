from rest_framework import filters
from django_filters import rest_framework
from .models import REF_PEGAWAI
 

class REF_PEGAWAIFilter(rest_framework.FilterSet):

    class Meta:
        model = REF_PEGAWAI
        fields = ['id_user','id_ref_lokasi']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
