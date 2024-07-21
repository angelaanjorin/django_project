from django.urls import path
from . import views
from .views import *


"""url paths"""
urlpatterns = [
    path('', views.JobsList.as_view(), name='jobs_list'),
    path('<slug:slug>/', views.job_detail, name='job_detail'),
    path('add_job/', views.Addjob.as_view(), name='add_job'),
    path('edit_job/<int:pk>', views.EditJob.as_view(), name='edit_job'),
    path('delete_job/<int:book_id>', views.delete_job, name='delete_job'),
    path('speciality/<speciality>/', views.SpecialityListView.as_view(),
          name='speciality'),
]