from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/up3-hari", views.TransTmUp3HariViews, basename='opsis-laporan-beban-up3-hari'
)

router.register(
    r"opsis/laporan-beban/up3-hari-pdf", views.LaporanUp3HariPDFViews, basename='opsis-laporan-beban-up3-hari-pdf'
)
