
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"trans/pm-jenis-doc", views.TransPmJenisDocViews, basename='trans-pm-jenis-doc'
) 