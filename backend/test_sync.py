
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'safepulse_backend.settings')
django.setup()

from django.test import RequestFactory
from tracker.views import SyncAPIView
from django.contrib.auth.models import User
try:
    user = User.objects.get(username='test@gmail.com')
    factory = RequestFactory()
    request = factory.get('sync/')
    request.user = user
    view = SyncAPIView.as_view()
    response = view(request)
    print(f'Status: {response.status_code}')
    if response.status_code == 200:
        print(f'Tracker length: {len(response.data.get("tracker", []))}')
        for l in response.data.get('tracker', []):
            print(f"{l.get('date')}: water={l.get('water')}")
    else:
        print(f'Error: {response.data}')
except Exception:
    import traceback
    print(traceback.format_exc())
