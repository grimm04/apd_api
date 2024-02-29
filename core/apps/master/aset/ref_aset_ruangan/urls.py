
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False)  

router.register(
    r"master/aset/ref-aset-ruangan", views.RefAsetRuanganViews, basename='aset-ref-aset-ruangan'
) 