from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/spectrum/rtl/digital", views.SCD_DIGITAL_RTLViews, basename='rtl-digital'
)
