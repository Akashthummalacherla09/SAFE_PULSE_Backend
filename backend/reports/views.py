from rest_framework import viewsets, permissions
from .models import Patient, ClinicalData
from .serializers import PatientSerializer, ClinicalDataSerializer

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ClinicalDataViewSet(viewsets.ModelViewSet):
    serializer_class = ClinicalDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ClinicalData.objects.filter(patient__user=self.request.user)
