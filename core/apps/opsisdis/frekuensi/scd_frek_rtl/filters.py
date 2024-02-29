from rest_framework import filters
from django_filters import rest_framework
from .models import FrekuensiRTL

class FrekuensiRTLFilter(rest_framework.FilterSet):

    datum_2 = rest_framework.DateTimeFilter(field_name='datum_2', label='datum_2 example: (2022-05-11 13:00:00 OR 2022-05-11 13:30:00)')

    class Meta:
        model = FrekuensiRTL
        fields = ['id_meter', 'datum_2']

class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)