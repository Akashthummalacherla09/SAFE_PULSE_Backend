from django.db import models
from django.contrib.auth.models import User

class HealthAssessment(models.Model):
    ASSESSMENT_TYPES = [
        ('heart', 'Heart'),
        ('kidney', 'Kidney'),
        ('liver', 'Liver'),
        ('lung', 'Lung'),
        ('cancer', 'Cancer'),
        ('brain', 'Alzheimer/Brain'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assessments')
    assessment_type = models.CharField(max_length=20, choices=ASSESSMENT_TYPES)
    inputs = models.JSONField()
    results = models.JSONField()
    score = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.user.username} - {self.assessment_type} ({self.timestamp})"
