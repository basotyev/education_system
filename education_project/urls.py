"""education_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import notifications
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView, RedirectView
from admin_api import views as vw

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("student.urls")),
    path('', include('django.contrib.auth.urls')),
    path('', include('rest_framework.urls')), # will add login button at the top right corner :)
    path('user_all/', vw.index, name='all'),
    path('create_user/', vw.create_user, name='create_user'),
    path('update_user/<int:id>', vw.update_user, name='update_user'),
    path('course_all/', vw.index_course, name='all'),
    path('create_course/', vw.create_course, name='create_user'),
    path('update_course/<int:id>', vw.update_course, name='update_user'),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
