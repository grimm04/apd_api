from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/subsistem-bulan", views.TransTmSubsistemBulanViews, basename='opsis-laporan-beban-subsistem-bulan'
)

router.register(
    r"opsis/laporan-beban/subsistem-bulan-pdf", views.LaporanSubSistemBulanPDFViews, basename='opsis-laporan-beban-subsistem-bulan-pdf'
)
