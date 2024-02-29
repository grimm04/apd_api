from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsisdis/ufr/penyulang", views.PenyulangUFRViews, basename='penyulang-ufr'
)
 