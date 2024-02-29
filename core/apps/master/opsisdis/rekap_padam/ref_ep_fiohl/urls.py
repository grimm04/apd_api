

from rest_framework import routers
from . import views  

router = routers.DefaultRouter(trailing_slash=False)
router.register( 
    r"master/opsisdis/ref-ep-fiohl", views.RefEpFiohlViews, basename='opsisdis-ref-ep-fiohl'
)  