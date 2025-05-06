from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/', views.apply_job, name='apply_job'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('applications/', views.application_list, name='application_list'),
]

# اضافه کردن مسیر فایل‌های مدیا فقط در حالت توسعه
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





