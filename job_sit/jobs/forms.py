from django import forms
from .models import JobApplication

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'email', 'phone', 'resume', 'cover_letter']
    
    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

