from numpy import source
from rest_framework import serializers

from .models import TelegramLog
from apps.master.fasop.telegram_bot.models import TelegramBot


class SubTelegramBotSerializer(serializers.ModelSerializer):
    bot_name = serializers.CharField(source='name')
    class Meta:
        model = TelegramBot
        fields = ['id_telegram_bot', 'nama', 'chat_code', 'status','bot_name']


class TelegramLogSerializers(serializers.ModelSerializer):
    id_chat = serializers.IntegerField(default=None)
    id_telegram_bot = serializers.SlugRelatedField(
        queryset=TelegramBot.objects.all(),
        slug_field='id_telegram_bot',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    telegram_bot = SubTelegramBotSerializer(read_only=True, source='id_telegram_bot')
    msg = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    status_sent = serializers.IntegerField(default=0)
    status = serializers.IntegerField(default=0)
    kirim_ulang = serializers.IntegerField(default=0)
    pesan_error = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    date_sent = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=None)

    class Meta:
        model = TelegramLog
        fields = '__all__'
