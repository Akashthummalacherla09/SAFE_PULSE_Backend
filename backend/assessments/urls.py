from django.urls import path
from .views import HealthAssessmentListCreateView, HealthAssessmentDetailView

urlpatterns = [
    path('', HealthAssessmentListCreateView.as_view(), name='assessment-list-create'),
    path('<int:pk>/', HealthAssessmentDetailView.as_view(), name='assessment-detail'),
]
