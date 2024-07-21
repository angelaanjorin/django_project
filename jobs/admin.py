from django.contrib import admin
from .models import Job, Speciality
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Job)
class JobsAdmin(SummernoteModelAdmin):
    """
    Admin for Jobs model
    """
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = 'review'
    list_display = ('title', 'slug', 'status', 'created_on','speciality', 'author', 'location', 'dates', 'link', 'review',)
    search_fields = ['title', 'review']