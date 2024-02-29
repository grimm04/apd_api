from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/trafo-gi-tahun", views.TransTmTrafoGiTahunViews, basename='opsis-laporan-beban-trafo-gi-tahun'
)

router.register(
    r"opsis/laporan-beban/trafo-gi-tahun-pdf", views.LaporanTrafoGiTahunPDFTESTViews, basename='opsis-laporan-beban-trafo-gi-tahun-pdf'
)
