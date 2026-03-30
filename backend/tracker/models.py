from django.db import models
from django.contrib.auth.models import User

class DailyLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='daily_logs')
    date = models.DateField()
    water = models.FloatField(default=0.0)
    smoked = models.BooleanField(default=False)
    steps = models.IntegerField(default=0)
    sleep = models.FloatField(default=0.0)
    calories = models.IntegerField(default=0)
    weight = models.FloatField(default=0.0)
    systolic = models.IntegerField(default=0)
    diastolic = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.username} - {self.date}"
