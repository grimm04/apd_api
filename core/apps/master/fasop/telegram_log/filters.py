from rest_framework import filters
from django_filters import rest_framework
from .models import TelegramLog


class TelegramLogFilter(rest_framework.FilterSet):

    class Meta:
        model = TelegramLog
        fields = ['id_telegram_bot', 'id_chat', 'status_sent', 'status', 'kirim_ulang']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
