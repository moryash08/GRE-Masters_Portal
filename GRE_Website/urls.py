from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='GRE_Website-home'),
    path('register/', views.register, name='GRE_Website-register'),
    path('login/', views.login, name='GRE_Website-login'),
    path('about/', views.about, name='GRE_Website-about'),
]
