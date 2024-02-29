from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/spectrum/kin/analog-bulan", views.SCD_KIN_ANALOG_BULANViews, basename='kin-analog-bulanan'
)
