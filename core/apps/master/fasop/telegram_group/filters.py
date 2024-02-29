from rest_framework import filters
from django_filters import rest_framework
from .models import TelegramGroup


class TelegramGroupFilter(rest_framework.FilterSet):

    class Meta:
        model = TelegramGroup
        fields = ['id_telegram_bot', 'nama', 'id_chat', 'status', 'datum_created']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
