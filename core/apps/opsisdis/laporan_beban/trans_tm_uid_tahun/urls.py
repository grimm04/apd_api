from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/uid-tahun", views.TransTmUidTahunViews, basename='opsis-laporan-beban-uid-tahun'
)

router.register(
    r"opsis/laporan-beban/uid-tahun-pdf", views.LaporanUIDTahunPDFViews, basename='opsis-laporan-beban-uid-tahun-pdf'
)

