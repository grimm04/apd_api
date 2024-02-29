from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/up3-tahun", views.TransTmUp3TahunViews, basename='opsis-laporan-beban-up3-tahun'
)
router.register(
    r"opsis/laporan-beban/up3-tahun-pdf", views.LaporanUp3TahunPDFViews, basename='opsis-laporan-beban-up3-tahun-pdf'
)
