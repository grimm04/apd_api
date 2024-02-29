

from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False)
router.register( 
    r"master/wilayah/ref-district", views.RefDistrictViews, basename='ref-district'
)  