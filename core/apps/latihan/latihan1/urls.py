from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"latihan/latihan1", views.Latihan1Views, basename='latihan1'
)