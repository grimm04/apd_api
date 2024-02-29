from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/penyulang-hari", views.TransTmPenyulangHariViews, basename='opsis-laporan-beban-penyulang-hari'
)
router.register(
    r"opsis/laporan-beban/penyulang-hari-pdf", views.LaporanPenyulangHariPDFTESTViews, basename='opsis-laporan-beban-penyulang-hari-pdf'
)
