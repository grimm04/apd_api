from rest_framework import filters
from django_filters import rest_framework
from .models import TransWoLogStatus


class TransWoLogStatusFilter(rest_framework.FilterSet):

    class Meta:
        model = TransWoLogStatus
        fields = ['id_ref_wo_status','id_wo', 'id_user_entri'] 
        
class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
