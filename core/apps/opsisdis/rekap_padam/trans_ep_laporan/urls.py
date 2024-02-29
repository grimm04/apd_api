
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False)  
router.register(
    r"opsisdis/rekap-padam/trans-ep-laporan", views.TransEpLaporanViews, basename='trans-ep-laporan'
) 