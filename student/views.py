from django.shortcuts import render
from .forms import EnrolleCourseForm
from admin_api.models import Course

# Create your views here.
def index(request):
    data = {
        'courses': Course.objects.all()
    }
    return render(request, 'index.html', data)

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

