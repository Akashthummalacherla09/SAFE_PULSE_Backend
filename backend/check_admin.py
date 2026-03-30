from django.contrib.auth.models import User
from accounts.models import Profile

u = User.objects.filter(username='admin@safepulse.com').first()
if u:
    print(f"User: {u.username}")
    print(f"Active: {u.is_active}")
    print(f"Staff: {u.is_staff}")
    if hasattr(u, 'profile'):
        print(f"Role: {u.profile.role}")
    else:
        print("No profile")
else:
    print("Admin user not found.")
