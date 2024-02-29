from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/spectrum/kin/rtu-harian", views.SCD_KIN_RTU_HARIANViews, basename='kin-digital-harian'
)
