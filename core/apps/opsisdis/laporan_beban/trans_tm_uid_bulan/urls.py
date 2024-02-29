from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/uid-bulan", views.TransTmUidBulanViews, basename='opsis-laporan-beban-uid-bulan'
)
router.register(
    r"opsis/laporan-beban/uid-bulan-pdf", views.LaporanUIDBulanPDFViews, basename='opsis-laporan-beban-uid-bulan-pdf'
)
