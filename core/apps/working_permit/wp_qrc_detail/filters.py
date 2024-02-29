from rest_framework import filters
from django_filters import rest_framework
from .models import WP_QRC_DETAIL
 

class WP_QRC_DETAILFilter(rest_framework.FilterSet):

    class Meta:
        model = WP_QRC_DETAIL
        fields = ['id_wp_qrc','id_pertanyaan_qrc','ada']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
