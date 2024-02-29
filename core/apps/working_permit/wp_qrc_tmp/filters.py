from rest_framework import filters
from django_filters import rest_framework
from .models import WP_QRC_TMP
 

class WP_QRC_TMPFilter(rest_framework.FilterSet):

    class Meta:
        model = WP_QRC_TMP
        fields = ['id_pertanyaan_qrc','ada']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
