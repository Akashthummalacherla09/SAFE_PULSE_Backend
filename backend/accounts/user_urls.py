from django.urls import path
from .views import ProfileView, UserDetailView

urlpatterns = [
    path('me/', UserDetailView.as_view(), name='user-detail'),
    path('profile/', ProfileView.as_view(), name='profile-detail'),
]
