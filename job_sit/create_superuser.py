# create_superuser.py

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "admin1234")
    print("✅ سوپر یوزر ساخته شد.")
else:
    print("ℹ️ سوپر یوزر از قبل وجود دارد.")
