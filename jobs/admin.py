from django.contrib import admin
from .models import Jobs, Employer, Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Jobs)
class JobsAdmin(SummernoteModelAdmin):
    """
    Admin for Trip model
    """
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = 'content'
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    """
    Add fields for Employer in admin panel
    """
    list_display = ('user',)
    search_fields = ['user']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Add fields for the profile in the admin panel
    """
    list_display = ('user',)