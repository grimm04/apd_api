from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)
from apps.authapi.views import CustomTokenObtainPairView

from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
#patches

from apps.api_urls import router as api_routers

# import view
from apps.users import views as UserSet
from apps.menu import views as MenuSet
from apps.roles import views as RoleSet
from apps.application_setting.views import ApplicationSettingByIDViews

 

router_reset_password = routers.DefaultRouter(trailing_slash=False)
router_reset_password.register(r"users/reset-user-password", UserSet.UsersResetPasswordView,
                               basename='users-reset-user-password')

urlpatterns = [
    # path('admin/', admin.site.urls),  
    path("apd/", include(router_reset_password.urls)),
    path("apd/", include(api_routers.urls)),
    path("apd/application-setting-detail/<int:pk>", ApplicationSettingByIDViews.as_view(), name="app-setting-byid"),
    path('apd/auth/', include('apps.authapi.urls', namespace='auth')), 
    path('apd/auth/login', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('apd/auth/refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
    path("apd/api/schema", SpectacularAPIView.as_view(), name="schema"),

    # test endpoint
    # path('apd/', include('apps.test_endpoint.urls')),

    path(
        "apd/api/docs/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html",
            url_name="schema"
        ),
        name="swagger-ui",
    ),
]
