from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    """
    Form for Jobs
    """
    class Meta:
        model = Job
        fields = ('title', 'author', 'location', 'speciality', 'dates', 'link', 'review')