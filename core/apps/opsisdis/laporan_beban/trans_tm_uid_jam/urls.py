from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/uid-jam", views.LaporanTransTmUidViews, basename='opsis-laporan-beban-uid-jam'
)

router.register(
    r"opsis/laporan-beban/uid-jam-pdf", views.LaporanUIDPDFViews, basename='opsis-laporan-beban-uid-jam-pdf'
)