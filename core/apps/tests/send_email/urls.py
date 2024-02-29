
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"tests/send-email", views.SendEmailViews, basename='tests-send-email'
) 