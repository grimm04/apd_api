from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/fasop/telegram-log", views.TelegramLogViews, basename='telegram-log'
)
