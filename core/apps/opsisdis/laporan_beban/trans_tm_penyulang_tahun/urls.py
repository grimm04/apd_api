from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/penyulang-tahun", views.TransTmPenyulangTahunViews, basename='opsis-laporan-beban-penyulang-tahun'
)

router.register(
    r"opsis/laporan-beban/penyulang-tahun-pdf", views.LaporanPenyulangTahunPDFTESTViews, basename='opsis-laporan-beban-penyulang-tahun-pdf'
)
