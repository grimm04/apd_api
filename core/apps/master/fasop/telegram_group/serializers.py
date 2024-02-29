from numpy import source
from rest_framework import serializers

from .models import TelegramGroup
from apps.master.fasop.telegram_bot.models import TelegramBot


class SubTelegramBotSerializer(serializers.ModelSerializer):
    bot_name = serializers.CharField(source='nama')
    class Meta:
        model = TelegramBot
        fields = ['id_telegram_bot', 'nama', 'chat_code', 'status','bot_name']


class TelegramGroupSerializers(serializers.ModelSerializer):
    id_telegram_bot = serializers.SlugRelatedField(
        queryset=TelegramBot.objects.all(),
        slug_field='id_telegram_bot',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    telegram_bot = SubTelegramBotSerializer(read_only=True, source='id_telegram_bot')
    nama = serializers.CharField(max_length=100)
    id_chat = serializers.IntegerField(default=None)
    status = serializers.IntegerField(default=None)
    datum_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = TelegramGroup
        fields = '__all__'
