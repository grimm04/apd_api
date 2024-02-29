from rest_framework import filters
from django_filters import rest_framework
from .models import Perusahaan


class PerusahaanFilter(rest_framework.FilterSet):

    class Meta:
        model = Perusahaan
        fields = ['nama_direktur','alamat_kantor','email','no_hp']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
