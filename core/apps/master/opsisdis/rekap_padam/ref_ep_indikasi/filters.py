from rest_framework import filters
from django_filters import rest_framework
from .models import RefEpIndikasi


class RefEpIndikasiFilter(rest_framework.FilterSet):

    class Meta:
        model = RefEpIndikasi
        fields = ['nama','jenis']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
