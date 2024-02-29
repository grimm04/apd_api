from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsis/laporan-beban/subsistem-hari", views.TransTmSubsistemHariViews, basename='opsis-laporan-beban-subsistem-hari'
)

router.register(
    r"opsis/laporan-beban/subsistem-hari-pdf", views.LaporanSubSistemHariPDFViews, basename='opsis-laporan-beban-subsistem-hari-pdf'
)
