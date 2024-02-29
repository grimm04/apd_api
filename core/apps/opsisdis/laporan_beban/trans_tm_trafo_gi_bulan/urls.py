from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/trafo-gi-bulan", views.TransTmTrafoGiBulanViews, basename='opsis-laporan-beban-trafo-gi-bulan'
)

router.register(
    r"opsis/laporan-beban/trafo-gi-bulan-pdf", views.LaporanTrafoGiBulanPDFTESTViews, basename='opsis-laporan-beban-trafo-gi-bulan-pdf'
)
