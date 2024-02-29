from django.db import models

# Create your models here.
from django.db import models

from apps.master.fasop.telegram_bot.models import TelegramBot


# Create your models here.
class TelegramGroup(models.Model):
    id_telegram_group = models.AutoField(primary_key=True)
    id_telegram_bot = models.ForeignKey(
        TelegramBot, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_telegram_bot'
    )
    nama = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    id_chat = models.IntegerField(blank=True, null=True, default=None)
    status = models.IntegerField(blank=True, null=True, default=None)
    datum_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scd_telegram_group'

    def __str__(self):
        return self.id_telegram_group

EXPORT_HEADERS = ['id_telegram_group', 'nama','id_chat', 'bot','status']
EXPORT_FIELDS = ['id_telegram_group','nama', 'id_chat','bot_name', 'status']
EXPORT_RELATION_FIELD = [
            {'telegram_bot':['bot_name']},  
] 