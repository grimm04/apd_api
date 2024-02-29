from rest_framework import filters
from django_filters import rest_framework
from .models import TelemetringPembangkit
from apps.opsisdis.telemetring.mapper import TelemetringMapper 
from library.date_converter import date_converter_dt

class TelemetringPembangkitFilter(rest_framework.FilterSet):
    TCHOICE = (
        ('True', True),
        ('False',False)
    )

    # i_null = rest_framework.ChoiceFilter(field_name='i',choices=TCHOICE, method='i_check',label='i check null')
    mapper = TelemetringMapper()
    # datum = rest_framework.DateFromToRangeFilter(field_name='datum', label='datum (30 Minutes) example: (2022-05-11 13:00 OR 2022-05-11 13:30)')
    datum_date = rest_framework.DateFilter(field_name='datum_date', method='filter_datum_date', label='datum example: (2022-05-11)')
    # tgl_entri_date = rest_framework.DateTimeFilter(field_name='tgl_entri_date', method='filter_tgl_entri_date', label='datum example: (2022-05-11)')


    def i_check(self, queryset, name, value):  
        return queryset.filter(i__isnull=value)

    def filter_datum_date(self, queryset, name, value):
        # datetime = self.mapper.date_mapper(date=value)
        start_date = date_converter_dt(date=value,time='00:00:00')
        end_date = date_converter_dt(date=value,time='23:59:00')  
        return queryset.filter(datum__range=(start_date,end_date))
        return queryset.filter(datum__gte=start_date.strftime("%Y-%m-%d %H:%M:%S.%f"),datum__lte=end_date.strftime("%Y-%m-%d %H:%M:%S.%f"))

    # def filter_tgl_entri_date(self, queryset, name, value):
    #     # datetime = self.mapper.date_mapper(date=value)
    #     return queryset.filter(tgl_entri__date=value)

    class Meta:
        model = TelemetringPembangkit
        fields = ['datum', 'id_lokasi', 'id_parent_lokasi']

class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)