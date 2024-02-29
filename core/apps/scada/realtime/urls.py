from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/scada/realtime", views.SCD_REALTIMETreeViews, basename='scd-realtime-tree'
)
 