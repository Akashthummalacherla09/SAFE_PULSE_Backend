from rest_framework import serializers
from .models import HealthAssessment

class HealthAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthAssessment
        fields = ['id', 'assessment_type', 'inputs', 'results', 'score', 'timestamp']
        read_only_fields = ['results', 'score', 'timestamp']
