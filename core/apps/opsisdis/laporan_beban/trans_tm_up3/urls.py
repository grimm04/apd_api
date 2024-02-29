from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/up3-jam", views.LaporanTransTmUp3JamViews, basename='opsis-laporan-beban-up3-jam'
)

router.register(
    r"opsis/laporan-beban/up3-jam-pdf", views.LaporanUP3PDFViews, basename='opsis-laporan-beban-up3-jam-pdf'
)
