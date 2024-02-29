from rest_framework import filters
from django_filters import rest_framework
from .models import TelemetringAMRCustomer

class TelemetringAMRCustomerFilter(rest_framework.FilterSet):

    class Meta:
        model = TelemetringAMRCustomer
        fields = ['customer_rid', 'meter_id', 'meter_type', 'rate', 'modem_adr', 'nama', 'alamat', 'lok', 'daya', 'bapm', 'faktor_kali', 'nofa', 'goltarif', 'kodegardu', 'id_lokasi']

class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)