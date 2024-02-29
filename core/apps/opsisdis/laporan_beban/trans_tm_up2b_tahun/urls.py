from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/up2b-tahun", views.TransTmUp2BTahunViews, basename='opsis-laporan-beban-up2b-tahun'
)

router.register(
    r"opsis/laporan-beban/up2b-tahun-pdf", views.LaporanUP2BTahunPDFViews, basename='opsis-laporan-beban-up2b-tahun-pdf'
)
