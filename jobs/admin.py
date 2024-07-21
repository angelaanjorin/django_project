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
    summernote_fields = 'review'
    list_display = ('title', 'slug', 'status', 'created_on','speciality', 'author', 'location', 'dates', 'link', 'review',)
    search_fields = ['title', 'author']

    admin.site.register(Speciality)