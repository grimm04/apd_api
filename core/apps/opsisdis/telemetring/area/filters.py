from rest_framework import filters
from django_filters import rest_framework
from .models import TelemetringArea

class TelemetringAreaFilter(rest_framework.FilterSet):

    # datum = rest_framework.DateTimeFilter(field_name='datum', label='datum (30 Minutes) example: (2022-05-11 13:00 OR 2022-05-11 13:30)')

    datum = rest_framework.DateTimeFilter(field_name='datum', label='datum (30 Minutes) example: (2022-05-11 13:00 OR 2022-05-11 13:30)')
    datum_date = rest_framework.DateTimeFilter(field_name='datum_date', method='filter_datum_date', label='datum example: (2022-05-11)')

 
    def filter_datum_date(self, queryset, name, value): 
        return queryset.filter(datum__date=value)
    class Meta:
        model = TelemetringArea
        fields = ['i', 'v', 'p', 'q', 'f', 'datum']

class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)