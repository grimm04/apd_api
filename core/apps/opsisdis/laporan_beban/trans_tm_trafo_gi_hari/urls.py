from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/trafo-gi-hari", views.TransTmTrafoGiHariViews, basename='opsis-laporan-beban-trafo-gi-hari'
)

router.register(
    r"opsis/laporan-beban/trafo-gi-hari-pdf", views.LaporanTrafoGiHariPDFTESTViews, basename='opsis-laporan-beban-trafo-gi-hari-pdf'
)
