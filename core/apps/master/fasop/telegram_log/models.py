from django.db import models
from apps.master.fasop.telegram_bot.models import TelegramBot


# Create your models here.
class TelegramLog(models.Model):
    id = models.AutoField(primary_key=True)
    id_chat = models.IntegerField(default=0, blank=True, null=True)
    id_telegram_bot = models.ForeignKey(
        TelegramBot, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_telegram_bot'
    )
    msg = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status_sent = models.IntegerField(default=0, blank=True, null=True)
    status = models.IntegerField(default=0, blank=True, null=True)
    kirim_ulang = models.IntegerField(default=0, blank=True, null=True)
    pesan_error = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    date_sent = models.DateTimeField(auto_now=True, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scd_trans_telegram_mess'

    def __str__(self):
        return self.id
    
EXPORT_HEADERS = ['id_telegram_group', 'msg','id_chat', 'bot','status_sent','status','kirim_ulang','pesan_error','pesan_error','date_sent']
EXPORT_FIELDS = ['id_telegram_group','msg', 'id_chat','bot_name', 'status_sent','status','kirim_ulang','pesan_error','pesan_error','date_sent']
EXPORT_RELATION_FIELD = [
            {'telegram_bot':['bot_name']},  
]
