from rest_framework import serializers
from .models import Patient, ClinicalData

class ClinicalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicalData
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    clinical_data = ClinicalDataSerializer(many=True, read_only=True)
    class Meta:
        model = Patient
        fields = '__all__'
