from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/up2b-jam", views.LaporanTransTmUp2BViews, basename='opsis-laporan-beban-up2b-jam'
)

router.register(
    r"opsis/laporan-beban/up2b-jam-pdf", views.LaporanUP2BPDFViews, basename='opsis-laporan-beban-up2b-jam-pdf'
)