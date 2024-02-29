# from django.urls import path
# from . import views


# urlpatterns = [
#     path('menu', views.CRMenuViews.as_view(), name='menu'),
#     path('menu/<int:menu_id>', views.ShowMenu.as_view(), name='admin'),
#     path('menu/<int:menu_id>', views.UDMenuViews.as_view(), name='manage_menu'),
# ]

from rest_framework import routers
from . import views  


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"menu", views.MenuViews, basename='menu'
)  
