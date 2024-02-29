from rest_framework import filters
from django_filters import rest_framework
from .models import RTU


class RTUFilter(rest_framework.FilterSet):

    class Meta:
        model = RTU
        fields = ['path3text', 'status', 'faktor', 'send_telegram', 'kinerja', 'id_pointtype', 'id_ref_lokasi']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
