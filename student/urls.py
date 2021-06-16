import notifications.urls
from django.conf.urls import url
from django.urls import path, include
from . import views
from admin_api import views as vw
from .views import *


app_name = "student"
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('students/', views.courses, name='courses'),
    path("register/", views.registerView, name="registration"),
    path("user/<username>", ProfileView.as_view(), name="profile"),
    path("login/", views.login_request, name="login"),
    path("admin_panel/", views.admin, name="admin"),
    path('team/python', views.python, name='python'),
    path('team/python_lesson1', views.pythonlesson1, name='python1'),
    path('team/python_lesson2', views.pythonlesson2, name='python2'),
    path('team/cpp', views.cpp, name='cpp'),
    path('team/cpp_lesson1', views.cpplesson1, name='cpp1'),
    path('teacher/', views.teacher, name='teacher'),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
]