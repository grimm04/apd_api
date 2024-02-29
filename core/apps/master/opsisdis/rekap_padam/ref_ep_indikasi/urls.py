

from rest_framework import routers
from . import views  

router = routers.DefaultRouter(trailing_slash=False)
router.register( 
    r"master/opsisdis/ref-ep-indikasi", views.RefEpIndikasiViews, basename='opsisdis-ref-ep-indikasi'
)  