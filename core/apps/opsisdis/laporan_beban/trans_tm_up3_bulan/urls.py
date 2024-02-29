from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/up3-bulan", views.TransTmUp3BulanViews, basename='opsis-laporan-beban-up3-bulan'
)

router.register(
    r"opsis/laporan-beban/up3-bulan-pdf", views.LaporanUp3BulanPDFViews, basename='opsis-laporan-beban-up3-bulan-pdf'
)
