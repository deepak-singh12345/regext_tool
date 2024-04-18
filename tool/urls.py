from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('check_regex/', views.check_regex, name='check_regex'),
]