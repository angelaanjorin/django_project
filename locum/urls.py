from . import views
from django.urls import path


urlpatterns = [
     path('<slug:slug>/', views.locum_detail.as_view(), name='locum_detail'),
     path('like/<slug:slug>', views.LocumLike.as_view(), name='locum_like'),
     path('section/<section>/', views.SecListView.as_view(),
          name='section'),
]