from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ApplicationForm

def home(request):
    return render(request, 'jobs/home.html')

def apply_job(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "درخواست شما با موفقیت ثبت شد. با تشکر!")
            return redirect('home')
    else:
        form = ApplicationForm()
    return render(request, 'jobs/apply.html', {'form': form})

def thank_you(request):
    return render(request, 'jobs/thank_you.html')
from django.contrib.auth.decorators import login_required
from .models import JobApplication

@login_required
def application_list(request):
    applications = JobApplication.objects.all().order_by('-created_at')
    return render(request, 'jobs/application_list.html', {'applications': applications})


