from rest_framework import filters
from django_filters import rest_framework
from .models import WP_MASTER_SOP_JSA
 

class WP_MASTER_SOP_JSAFilter(rest_framework.FilterSet):

    class Meta:
        model = WP_MASTER_SOP_JSA
        fields = ['id_wp_master_bagian','judul_pekerjaan']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
