from . import views
from django.urls import path


urlpatterns = [
     path('', views.JobsList.as_view(), name='jobs'),
     path('<slug:slug>/', views.JobDetail.as_view(), name='job_detail'),
     path('<slug:slug>/edit_job/<int:job_id>',
          views.EditJob.as_view(), name='edit_job'),
     path('<slug:slug>/delete_job/<int:job_id>',
          views.delete_job, name='delete_job'),

]