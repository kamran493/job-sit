from django.db import models

class JobApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    cover_letter = models.TextField()
    resume_file = models.FileField(upload_to='resumes/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)  # تاریخ ارسال درخواست

    def __str__(self):
        return self.name
