from django.urls import path
from .views import UserManagementView, GlobalReportsView, UserDeleteView, UserUpdateView

urlpatterns = [
    path('users/', UserManagementView.as_view(), name='admin-users'),
    path('users/<int:id>/update/', UserUpdateView.as_view(), name='admin-user-update'),
    path('users/<int:id>/delete/', UserDeleteView.as_view(), name='admin-user-delete'),
    path('reports/', GlobalReportsView.as_view(), name='admin-reports'),
]
