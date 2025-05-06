from django.contrib import admin
from .models import JobApplication
from django.utils.html import format_html

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'submitted_at', 'download_resume')
    list_filter = ('submitted_at',)
    search_fields = ('name', 'email', 'phone')

    def download_resume(self, obj):
        if obj.resume:
            return format_html(f'<a href="{obj.resume.url}" target="_blank">دانلود رزومه</a>')
        return 'ندارد'

    download_resume.short_description = "رزومه"
