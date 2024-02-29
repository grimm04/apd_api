

from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False)
router.register( 
    r"master/wilayah/ref-regency", views.RefRegencyViews, basename='ref-regency'
)  