from rest_framework import filters
from django_filters import rest_framework
from .models import JenisPenyebabGangguan


class JenisPenyebabGangguanFilter(rest_framework.FilterSet):

    class Meta:
        model = JenisPenyebabGangguan
        fields = []


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
