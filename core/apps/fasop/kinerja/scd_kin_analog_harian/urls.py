from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/spectrum/kin/analog-hari", views.SCD_KIN_ANALOG_HARIANViews, basename='kin-analog-harian'
)
