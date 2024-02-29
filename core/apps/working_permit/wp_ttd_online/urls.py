from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"working-permit/ttd-online", views.WP_TTD_ONLINEViews, basename='wp-ttd-online'
)
