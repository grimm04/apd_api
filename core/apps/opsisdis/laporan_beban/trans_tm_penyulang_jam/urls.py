from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/penyulang-jam", views.LaporanPenyulangViews, basename='opsis-laporan-beban-penyulang-jam'
)
router.register(
    r"opsis/laporan-beban/penyulang-jam-pdf", views.LaporanPenyulangPDFTESTViews, basename='opsis-laporan-beban-penyulang-jam-pdf'
)
