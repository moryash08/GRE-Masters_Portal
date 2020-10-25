from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='GRE_Website-home'),
    path('about/', views.about, name='GRE_Website-about'),
    path('university-form/', views.universityform, name='university-form'),
]
