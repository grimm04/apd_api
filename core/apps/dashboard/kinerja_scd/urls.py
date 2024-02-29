from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"dashboard_kinerja/kinerja_box_bulanan_rtu", views.DashboardKinerjaScdBoxBulananRTUView, basename='kinerja-box-bulanan-rtu'
)
router.register(
    r"dashboard_kinerja/kinerja_box_bulanan_master", views.DashboardKinerjaScdBoxBulananMASTERView, basename='kinerja-box-bulanan-master'
)
router.register(
    r"dashboard_kinerja/kinerja_box_bulanan_telkom", views.DashboardKinerjaScdBoxBulananTELKOMView, basename='kinerja-box-bulanan-telkom'
)
router.register(
    r"dashboard_kinerja/kinerja_box_bulanan_rc", views.DashboardKinerjaScdBoxBulananRCView, basename='kinerja-box-bulanan-rc'
)


router.register(
    r"dashboard_kinerja/kinerja_box_komulatif_master", views.DashboardKinerjaScdBoxKOMULATIFMASTERView, basename='kinerja-box-komulatif-master'
)
router.register(
    r"dashboard_kinerja/kinerja_box_komulatif_rtu", views.DashboardKinerjaScdBoxKOMULATIFRTUView, basename='kinerja-box-komulatif-rtu'
)
router.register(
    r"dashboard_kinerja/kinerja_box_komulatif_telkom", views.DashboardKinerjaScdBoxKOMULATIFTELKOMView, basename='kinerja-box-komulatif-telkom'
)
router.register(
    r"dashboard_kinerja/kinerja_box_komulatif_rc", views.DashboardKinerjaScdBoxKOMULATIFRCView, basename='kinerja-box-komulatif-rc'
)


router.register(
    r"dashboard_kinerja/kinerja_grafik_rtu", views.DashboardKinerjaScdGrafikRTUView, basename='kinerja-grafik-rtu'
)
router.register(
    r"dashboard_kinerja/kinerja_grafik_master", views.DashboardKinerjaScdGrafikMASTERView, basename='kinerja-grafik-master'
)
router.register(
    r"dashboard_kinerja/kinerja_grafik_telkom", views.DashboardKinerjaScdGrafikTELKOMView, basename='kinerja-grafik-telkom'
)
router.register(
    r"dashboard_kinerja/kinerja_grafik_rc", views.DashboardKinerjaScdGrafikRCView, basename='kinerja-grafik-rc'
)


router.register(
    r"dashboard_kinerja/kinerja_box_rtu_gi", views.DashboardKinerjaScdBoxRTUGIView, basename='kinerja-box-rtu-gi'
)
router.register(
    r"dashboard_kinerja/kinerja_box_rtu_gh", views.DashboardKinerjaScdBoxRTUGHView, basename='kinerja-box-rtu-gh'
)
router.register(
    r"dashboard_kinerja/kinerja_box_rtu_sso", views.DashboardKinerjaScdBoxRTUSSOView, basename='kinerja-box-rtu-sso'
)
router.register(
    r"dashboard_kinerja/kinerja_box_rtu_rcl", views.DashboardKinerjaScdBoxRTURCLView, basename='kinerja-box-rtu-rcl'
)


router.register(
    r"dashboard_kinerja/kinerja_box_rtu_in_pool", views.DashboardKinerjaScdBoxRTUINView, basename='kinerja-box-rtu-in-pool'
)
router.register(
    r"dashboard_kinerja/kinerja_box_rtu_out_pool", views.DashboardKinerjaScdBoxRTUOUTView, basename='kinerja-box-rtu-out-pool'
)


router.register(
    r"dashboard_kinerja/kinerja_box_rtu_out__off_pool", views.DashboardKinerjaScdBoxRTUOUOFFPOOLView, basename='kinerja-box-rtu-out-off-pool'
)
