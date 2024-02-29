from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/spectrum/kin/digital-hari", views.SCD_KIN_DIGITAL_HARIViews, basename='kin-digital-harian'
)
