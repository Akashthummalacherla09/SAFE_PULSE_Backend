from django.urls import path
from .views import DailyLogListCreateView

urlpatterns = [
    path('', DailyLogListCreateView.as_view(), name='tracker-list-create'),
]
