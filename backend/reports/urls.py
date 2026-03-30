from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, ClinicalDataViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'clinical-data', ClinicalDataViewSet, basename='clinical-data')

urlpatterns = [
    path('', include(router.urls)),
]
