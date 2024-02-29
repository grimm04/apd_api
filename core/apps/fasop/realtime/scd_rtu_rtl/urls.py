from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/spectrum/rtl/rtu", views.SCD_RTU_RTLViews, basename='rtl-rtu'
)
