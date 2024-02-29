from rest_framework import filters
from django_filters import rest_framework
from .models import WP_APROVAL_TTD
 

class WP_APROVAL_TTDFilter(rest_framework.FilterSet):

    class Meta:
        model = WP_APROVAL_TTD
        fields = ['id_user','id_wp_master_bagian']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
