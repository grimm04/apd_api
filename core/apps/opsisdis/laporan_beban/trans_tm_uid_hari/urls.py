from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/uid-hari", views.TransTmUidHariViews, basename='opsis-laporan-beban-uid-hari'
)
