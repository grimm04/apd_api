from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/up2b-bulan", views.TransTmUp2BBulanViews, basename='opsis-laporan-beban-up2b-bulan'
)


router.register(
    r"opsis/laporan-beban/up2b-bulan-pdf", views.LaporanUP2BBulanPDFViews, basename='opsis-laporan-beban-up2b-bulan-pdf'
)
