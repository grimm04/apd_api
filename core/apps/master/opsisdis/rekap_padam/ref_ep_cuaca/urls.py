

from rest_framework import routers
from . import views  

router = routers.DefaultRouter(trailing_slash=False)
router.register( 
    r"master/opsisdis/ref-ep-cuaca", views.RefEpCuacaViews, basename='opsisdis-ref-ep-cuaca'
)  