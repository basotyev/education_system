from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from admin_api.models import Course
from .forms import EnrolleCourseForm, SimpleUserForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return  render(request, 'about.html')

def team(request):
    return  render(request, 'team.html')

def courses(request):
    if request.method == 'POST':
        form = EnrolleCourseForm(request.POST)
        if form.is_valid():
            form.save()
    form = EnrolleCourseForm()
    courses = Course.objects.all()
    data = {
        'form': form,
        'courses': courses
    }
    return render(request, 'student/index.html', data)

class registerView(CreateView):
    form_class = SimpleUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'

class ProfileView(TemplateView):
    template_name = "registration/user_page.html"