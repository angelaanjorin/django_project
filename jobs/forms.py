from .models import Jobs, Profile
from django.contrib.auth.models import User
from django import forms

class JobsForm(forms.ModelForm):
    """
    Job creator/editor form
    """
    class Meta:
        model = Jobs
        fields = (
            'title',
            'dates',
            'location',
            'speciality',
            'job_info',
        )

class UserUpdateForm(forms.ModelForm):
    """
    Form for user details update
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    """
    Form for profile update
    """
    class Meta:
        model = Profile
        fields = [
            'firstname', 
            'surname', 
            'speciality', 
            'email', 
            'phone_number', 
            'cv', 
            'user_picture'
        ]
