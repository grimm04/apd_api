from rest_framework import filters
from django_filters import rest_framework
from .models import REF_REGU_PETUGAS_MODELS


class REF_REGU_PETUGASFilter(rest_framework.FilterSet):

    class Meta:
        model = REF_REGU_PETUGAS_MODELS
        fields = []


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
