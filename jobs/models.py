from django.db import models
from django.utils import timezone

class JobApplication(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    phone = models.CharField(max_length=15, verbose_name="شماره تماس")
    resume_file = models.FileField(upload_to='resumes/', verbose_name="فایل رزومه", blank=True, null=True)
    resume_text = models.TextField(verbose_name="توضیحات رزومه", blank=True)
    cover_letter = models.TextField(verbose_name="متن درخواست", blank=True)
    submitted_at = models.DateTimeField(default=timezone.now, verbose_name="زمان ارسال")

    def __str__(self):
        return self.name
