# reset_admin.py
from django.contrib.auth import get_user_model

User = get_user_model()
username = "newadmin"
new_password = "12345678Aa"  # رمز جدید که خودت می‌خوای

try:
    user = User.objects.get(username=username)
    user.set_password(new_password)
    user.save()
    print("رمز جدید با موفقیت تنظیم شد.")
except User.DoesNotExist:
    print("کاربری با این نام وجود ندارد.")
