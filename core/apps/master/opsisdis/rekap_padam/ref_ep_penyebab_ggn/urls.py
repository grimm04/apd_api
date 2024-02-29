

from rest_framework import routers
from . import views  

router = routers.DefaultRouter(trailing_slash=False)
router.register( 
    r"master/opsisdis/ref-ep-penyebab-ggn", views.RefEpPenyebabGgnViews, basename='opsisdis-ref-ep-penyebab-ggn'
)  