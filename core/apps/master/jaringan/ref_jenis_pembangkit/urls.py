

from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False)
router.register( 
    r"master/jaringan/ref-jenis-pembangkit", views.RefJenisPembangkitViews, basename='jaringan-ref-jenis-pembangkit'
)  