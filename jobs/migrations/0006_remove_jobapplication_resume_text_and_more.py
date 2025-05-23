# Generated by Django 5.2 on 2025-05-12 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_remove_jobapplication_resume_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='resume_text',
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='cover_letter',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='resume_file',
            field=models.FileField(blank=True, null=True, upload_to='resumes/'),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='submitted_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
