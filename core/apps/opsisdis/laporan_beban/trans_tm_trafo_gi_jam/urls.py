from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/trafo-gi-jam", views.LaporanTrafoGIViews, basename='opsis-laporan-beban-trafo-gi-jam'
)

router.register(
    r"opsis/laporan-beban/trafo-gi-jam-pdf", views.LaporanTrafoGIPDFTESTViews, basename='opsis-laporan-beban-trafo-gi-jam-pdf'
)
