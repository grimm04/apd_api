from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/subsistem-tahun", views.TransTmSubsistemTahunViews, basename='opsis-laporan-beban-uid-tahun'
)

router.register(
    r"opsis/laporan-beban/subsistem-tahun-pdf", views.LaporanSubSistemTahunPDFViews, basename='opsis-laporan-beban-subsistem-tahun-pdf'
)
