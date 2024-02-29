

from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False)
router.register( 
    r"master/jaringan/ref-jenis-lokasi", views.RefJenisLokasiViews, basename='jaringan-ref-jenis-lokasi'
)  