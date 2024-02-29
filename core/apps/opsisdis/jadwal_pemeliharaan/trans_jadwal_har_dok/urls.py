
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False)  
router.register(
    r"opsisdis/jadwal-pemeliharaan/trans-jadwal-har-dok", views.TransJadwalHarDokViews, basename='trans-jadwal-har-dok'
) 