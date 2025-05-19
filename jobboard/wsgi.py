"""
WSGI config for jobboard project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobboard.settings')

application = get_wsgi_application()
# job_sit/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_sit.settings')
application = get_wsgi_application()

# --- کد اجرای reset_admin ---
try:
    from reset_admin import *
except Exception as e:
    print("خطا در تغییر رمز:", e)
