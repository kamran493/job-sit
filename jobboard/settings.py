import os
import dj_database_url
from pathlib import Path

# مسیر اصلی پروژه
BASE_DIR = Path(__file__).resolve().parent.parent

# امنیت و تنظیمات عمومی
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-default-key')  # مقدار از محیط خوانده شود
DEBUG = os.getenv('DEBUG', 'True') == 'True'  # مقدار از محیط خوانده شود

# تنظیمات هاست‌های مجاز
ALLOWED_HOSTS = [
    "jobboard-xdzg.onrender.com",  # آدرس سایت در Render
    "127.0.0.1",  # برای تست محلی
    "localhost",  # برای تست محلی
]

# اپلیکیشن‌های نصب‌شده
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jobs',
    'crispy_forms',
    'crispy_bootstrap5',
]

# میان‌افزارها
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # فعال‌سازی Whitenoise برای فایل‌های استاتیک
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# تنظیمات مسیرهای URL
ROOT_URLCONF = 'jobboard.urls'

# تنظیمات WSGI
WSGI_APPLICATION = 'jobboard.wsgi.application'

# تنظیم پایگاه داده
DATABASE_URL = os.getenv('DATABASE_URL')

if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=600, ssl_require=True)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'jobsit',  # نام پایگاه داده صحیح
            'USER': 'kamran493',  # نام کاربری صحیح
            'PASSWORD': 'X71AqfabdCzB0dKLlmUnXHxY130c53Af',  # رمز عبور صحیح
            'HOST': 'dpg-d0cottumcj7s73apvsl0-a',  # نام هاست صحیح
            'PORT': '5432'  # پورت صحیح
        }
    }


# تنظیمات احراز هویت
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# تنظیمات بین‌المللی
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# مسیر فایل‌های استاتیک
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# مسیر فایل‌های رسانه‌ای
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# تنظیم `crispy_forms`
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# نوع پیش‌فرض کلید‌های دیتابیس
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # اضافه کردن مسیر قالب‌ها
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
import os

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'