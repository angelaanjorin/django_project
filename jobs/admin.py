from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . import models
from .models import Job, Speciality


@admin.register(Job)
class JobsAdmin(SummernoteModelAdmin):
    """
    Admin for Jobs model
    """
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = 'job_description'
    list_display = ('title', 'status', 'created_on', 'author','start_date', 'end_date')
    search_fields = ['title', 'author']

    admin.site.register(models.Speciality)