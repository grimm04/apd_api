from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/up2b-hari", views.TransTmUp2BHariViews, basename='opsis-laporan-beban-up2b-hari'
)

router.register(
    r"opsis/laporan-beban/up2b-hari-pdf", views.LaporanUP2BHariPDFViews, basename='opsis-laporan-beban-up2b-hari-pdf'
)
