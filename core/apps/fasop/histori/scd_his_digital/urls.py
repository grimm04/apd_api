from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/spectrum/his/digital", views.SCD_HIS_DIGITALViews, basename='his-digital'
)
