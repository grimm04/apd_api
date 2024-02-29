from rest_framework import filters
from django_filters import rest_framework
from .models import PertanyaanQRC

class PertanyaanQRCFilter(rest_framework.FilterSet):

    class Meta:
        model = PertanyaanQRC
        fields = ['pertanyaan_qrc', 'pertanyaan_qrc_point']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
