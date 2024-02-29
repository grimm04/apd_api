# from django.urls import path
# from . import views


# urlpatterns = [
#     path('roles', views.CRRolesViews.as_view(), name='roles'),
#     path('roles/<int:role_id>', views.UDRolesViews.as_view(), name='manage_roles'),
# ]

from rest_framework import routers
from . import views  


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"roles", views.RolesViews, basename='roles'
)  
