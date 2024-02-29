from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/working-permit/larangan-tanggung-jawab-mitra", views.LaranganTanggungJawabMitraView, basename='larangan-tanggung-jawab-mitra'
)