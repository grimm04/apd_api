from rest_framework import filters
from django_filters import rest_framework
from .models import PointTypeState


class PointTypeStateFilter(rest_framework.FilterSet):

    class Meta:
        model = PointTypeState
        fields = ['id_pointtype', 'status', 'valid', 'date_created', 'statekey', 'quality_code']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
