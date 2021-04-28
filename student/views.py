from django.shortcuts import render
from admin_api.models import Course
from .forms import EnrolleCourseForm


# Create your views here.
def index(request):
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

