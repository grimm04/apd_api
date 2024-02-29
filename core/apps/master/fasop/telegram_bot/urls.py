from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/fasop/telegram-bot", views.TelegramBotViews, basename='telegram-bot'
)
