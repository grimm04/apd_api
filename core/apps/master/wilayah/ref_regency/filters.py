from rest_framework import filters
from django_filters import rest_framework
from .models import RefRegency


class RefRegencyFilter(rest_framework.FilterSet):

    class Meta:
        model = RefRegency
        fields = ['name','id_ref_province']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
