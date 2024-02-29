from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/spectrum/rtl/master", views.SCD_MASTER_RTLViews, basename='rtl-master'
)
