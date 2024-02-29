from rest_framework import filters
from django_filters import rest_framework
from .models import ApprovalManagementWP

class ApprovalManagementWPFilter(rest_framework.FilterSet):

    class Meta:
        model = ApprovalManagementWP
        fields = ['nama_pegawai', 'nama_jabatan']

class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
