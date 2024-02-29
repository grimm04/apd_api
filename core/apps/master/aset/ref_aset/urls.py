
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"master/aset/ref-aset", views.RefAsetViews, basename='aset-ref-aset'
) 