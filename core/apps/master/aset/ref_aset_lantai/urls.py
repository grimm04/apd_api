
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False)  

router.register(
    r"master/aset/ref-aset-lantai", views.RefAsetLantaiViews, basename='aset-ref-aset-lantai'
) 