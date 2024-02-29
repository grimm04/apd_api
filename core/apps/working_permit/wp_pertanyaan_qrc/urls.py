from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"working-permit/pertanyaan-qrc", views.WP_PERTANYAAN_QRCViews, basename='wp-pertanyaan-qrc'
)
