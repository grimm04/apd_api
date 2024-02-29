
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"master/aset/ref-aset-doc", views.RefAsetDocViews, basename='aset-ref-aset-doc'
) 