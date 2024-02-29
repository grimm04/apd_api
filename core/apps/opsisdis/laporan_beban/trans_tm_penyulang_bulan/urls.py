from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/penyulang-bulan", views.TransTmPenyulangBulanViews, basename='opsis-laporan-beban-penyulang-bulan'
)

router.register(
    r"opsis/laporan-beban/penyulang-bulan-pdf", views.LaporanPenyulangBulanPDFTESTViews, basename='opsis-laporan-beban-penyulang-bulan-pdf'
)
