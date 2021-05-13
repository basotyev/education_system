from django.urls import path, include
from . import views

app_name = "student"
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('students/', views.courses, name='courses')
]