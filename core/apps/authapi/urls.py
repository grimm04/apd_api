from django.urls import path
from .views import CustomUserCreate, LogoutAllView, AuthDetailsView, ChangePasswordView

app_name = 'users'

urlpatterns = [
    path('register', CustomUserCreate.as_view(), name="register"),
    path('change-password/<int:pk>', ChangePasswordView.as_view(), name='auth_change_password'),
    path('details', AuthDetailsView.as_view(), name="details"),
    path('logout', LogoutAllView.as_view(),
         name='logout')
]
