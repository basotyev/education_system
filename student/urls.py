from django.urls import path, include
from . import views
from .views import *

app_name = "student"
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('students/', views.courses, name='courses'),
    path("register/", registerView.as_view(), name="registration"),
    path("user/<username>", ProfileView.as_view(), name="profile"),
]