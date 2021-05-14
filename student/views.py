from django.shortcuts import render
from admin_api.models import Course
from .forms import EnrolleCourseForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

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

