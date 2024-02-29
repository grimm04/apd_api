from rest_framework import filters
from django_filters import rest_framework
from .models import Frekuensi5M
from datetime import datetime

class Frekuensi5MFilter(rest_framework.FilterSet):

    datum_2 = rest_framework.DateTimeFilter(field_name='datum_2', label='datum_2 example: (2022-05-11 OR 2022-05-12)',
                                            method='filter_datum')

    def filter_datum(self, queryset, name, value):
        if type(value) != str:
            value = value.strftime('%Y-%m-%d')
        date = datetime.strptime(value, '%Y-%m-%d')
        return queryset.filter(datum_2__date=date)

    class Meta:
        model = Frekuensi5M
        fields = ['id_meter', 'datum_2']

class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)