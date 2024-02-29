from rest_framework import filters
from django_filters import rest_framework
from .models import TelemetringAMRLoadProfile

class TelemetringAMRLoadProfileFilter(rest_framework.FilterSet):

    tgl = rest_framework.DateTimeFilter(field_name='tgl', label='tgl example: (2022-05-11 13:00:00 OR 2022-05-11 13:30:00)')

    class Meta:
        model = TelemetringAMRLoadProfile
        fields = ['customer_rid', 'tgl']

class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)