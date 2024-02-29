from rest_framework import filters
from django_filters import rest_framework
from .models import RefDistrict


class RefDistrictFilter(rest_framework.FilterSet):

    class Meta:
        model = RefDistrict
        fields = ['name','id_ref_regency']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
