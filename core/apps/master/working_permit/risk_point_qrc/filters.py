from rest_framework import filters
from django_filters import rest_framework
from .models import RiskPointQRC

class RiskPointQRCFilter(rest_framework.FilterSet):

    class Meta:
        model = RiskPointQRC
        fields = ['low_risk_point_min', 'low_risk_point_max', 'medium_risk_point_min', 'medium_risk_point_max', 'high_risk_point']

class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
