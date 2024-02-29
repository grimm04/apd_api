from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/spectrum/rtl/analog", views.SCD_ANALOG_RTLViews, basename='rtl-analog'
)
