from . import views
from django.urls import path
from users import views as user_views


urlpatterns = [
    path('', views.home, name='GRE_Website-home'),
    path('about/', views.about, name='GRE_Website-about'),
    path('form/', views.universityform, name='GRE_Website-universityform'),
    path('register/', user_views.register, name='users-register'),
    path('login/', user_views.login, name='users-login'),
]
