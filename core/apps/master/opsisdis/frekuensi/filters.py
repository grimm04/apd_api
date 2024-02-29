from rest_framework import filters
from django_filters import rest_framework
from .models import Frekuensi

class FrekuensiFilter(rest_framework.FilterSet):

    class Meta:
        model = Frekuensi
        fields = ['nama', 'lokasi']

class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
