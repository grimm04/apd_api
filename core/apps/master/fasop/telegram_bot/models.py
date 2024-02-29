from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class TelegramBot(models.Model):
    id_telegram_bot = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    chat_code = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status = models.IntegerField(blank=True, null=True, default=None)
    datum_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scd_telegram_bot'

    def __str__(self):
        return self.id_telegram_bot


EXPORT_HEADERS = ['id_telegram_bot', 'nama','chat_code', 'status']
EXPORT_FIELDS = ['id_telegram_bot','nama', 'chat_code', 'status']
EXPORT_RELATION_FIELD = [ ] 