from django.urls import path
from .views import RegisterView, LoginAPIView, CheckEmailView, PasswordResetView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('check-email/', CheckEmailView.as_view(), name='check-email'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
]
