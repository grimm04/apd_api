from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/subsistem-jam", views.LaporanTransTmSubsistemViews, basename='opsis-laporan-beban-subsistem-jam'
)

router.register(
    r"opsis/laporan-beban/subsistem-jam-pdf", views.LaporanSubSistemPDFViews, basename='opsis-laporan-beban-subsistem-jam-pdf'
)