from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/spectrum/his/analog-30m", views.SCD_ANALOG_HIS_30MViews, basename='his-analog-30m'
)
