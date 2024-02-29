
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False)  
router.register(
    r"opsisdis/jadwal-pemeliharaan/trans-jadwal-har-gardu", views.TransJadwalHarGarduViews, basename='trans-jadwal-har-gardu'
) 