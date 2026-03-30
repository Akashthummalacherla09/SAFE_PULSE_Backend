from django.contrib import admin
from django.urls import path, include
from accounts.views import LoginAPIView, RegisterView, CheckEmailView, PasswordResetView
from tracker.views import SyncAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Unified Auth APIs
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginAPIView.as_view(), name='login'),
    path('api/check-email/', CheckEmailView.as_view(), name='check-email'),
    path('api/reset-password/', PasswordResetView.as_view(), name='reset-password'),
    
    # Patients & Clinical Data APIs
    path('api/', include('reports.urls')),
    
    # Health Assessment APIs
    path('api/assessments/', include('assessments.urls')),
    
    # Tracker & Sync APIs
    path('api/tracker/', include('tracker.urls')),
    path('api/sync/', SyncAPIView.as_view(), name='sync'),
    path('api/admin/', include('admin_panel.urls')),
]
