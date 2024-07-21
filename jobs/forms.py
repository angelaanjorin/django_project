from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    """
    Form for Jobs
    """
    class Meta:
        model = Job
        fields = ('title', 'author', 'location', 'speciality', 'start_date', 'end_date', 'link', 'job_description')
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'placeholder': '01.09.2024'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'placeholder': '31.12.2024'}),
        }