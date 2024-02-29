from rest_framework import filters
from django_filters import rest_framework
from .models import WP_HIRARC
 

class WP_HIRARCFilter(rest_framework.FilterSet):

    class Meta:
        model = WP_HIRARC
        fields = ['id_wp_master_bagian','tanggal','lokasi_pekerjaan','pekerjaan']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
