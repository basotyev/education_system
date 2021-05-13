from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='about'),
    path('about.html', views.about, name='about'),
    path('students/', views.courses, name='courses')
]