from django.urls import path
from .views import GroupEndpointViews, GroupAccessEndpointViews

app_name = 'group'

urlpatterns = [
    path('group', GroupEndpointViews.as_view(), name='group'),
    path('group_access', GroupAccessEndpointViews.as_view(), name='group_access'),
]
