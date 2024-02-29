from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/spectrum/kin/rtu-bulan", views.SCD_KIN_RTU_BULANViews, basename='kin-digital-bulan'
)
