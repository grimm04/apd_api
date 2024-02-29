from rest_framework import filters
from django_filters import rest_framework
from .models import TelemetringTrafoGI
from apps.opsisdis.telemetring.mapper import TelemetringMapper
from library.date_converter import date_converter_dt 
class TelemetringTrafoGIFilter(rest_framework.FilterSet):

    mapper = TelemetringMapper()
    # datum = rest_framework.DateTimeFilter(field_name='datum', label='datum (30 Minutes) example: (2022-05-11 13:00 OR 2022-05-11 13:30)')
    # jenis_layanan 
    # def filter_datum(self, queryset, name, value):
    #     datetime = self.mapper.date_mapper(date=value)
    #     return queryset.filter(datum__date=datetime, datum__hour=datetime.hour, datum__minute=datetime.minute)

    datum = rest_framework.DateTimeFilter(field_name='datum', label='datum (30 Minutes) example: (2022-05-11 13:00 OR 2022-05-11 13:30)')
    datum_date = rest_framework.DateFilter(field_name='datum_date', method='filter_datum_date', label='datum example: (2022-05-11)')

 
    def filter_datum_date(self, queryset, name, value): 
        start_date = date_converter_dt(date=value,time='00:00:00')
        end_date = date_converter_dt(date=value,time='23:59:00')  
        return queryset.filter(datum__range=(start_date,end_date)) 

    class Meta:
        model = TelemetringTrafoGI
        fields = ['datum', 'id_lokasi', 'id_parent_lokasi']

class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)