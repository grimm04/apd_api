from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/spectrum/kin/digital-bulan", views.SCD_KIN_DIGITAL_BULANViews, basename='kin-digital-bulanan'
)
