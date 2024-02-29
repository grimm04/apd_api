from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/scada/histori", views.SCD_HISTORITreeViews, basename='scd-histori-tree'
)
 