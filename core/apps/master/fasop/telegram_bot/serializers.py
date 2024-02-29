from rest_framework import serializers

from .models import TelegramBot


class TelegramBotSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=100)
    chat_code = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    status = serializers.IntegerField()
    datum_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = TelegramBot
        fields = '__all__'
