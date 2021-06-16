from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect

from student.models import SimpleUser
from .models import User
from student.forms import NewUserForm
from .models import Course
from .forms import CourseForm
from django.http import HttpResponse


def index(request):
    all = SimpleUser.objects.all()
    return render(request, "all_users.html", {"all": all})


def create_user(request):
    create = NewUserForm()
    if request.method == 'POST':
        create = NewUserForm(request.POST, request.FILES)
        if create.is_valid():
            create.save()
            return redirect('create_user')
        else:
            return HttpResponse('ERROR!')
    else:
        return render(request, "create_user.html", {"create": create})


def update_user(request, id):
    id = int(id)
    try:
        userid = User.objects.get(id=id)
    except User.DoesNotExist:
        return redirect('about')
    update = NewUserForm(request.POST or None, id)
    if update.is_valid():
        update.save()
    return render(request, "update_user.html", {"update": update})


def index_course(request):
    all = Course.objects.all()
    return render(request, "all_users.html", {"all": all})


def create_course(request):
    create = CourseForm()
    if request.method == 'POST':
        create = CourseForm(request.POST, request.FILES)
        if create.is_valid():
            create.save()
            return redirect('create_course')
        else:
            return HttpResponse('ERROR!')
    else:
        return render(request, "create_user.html", {"create": create})


def update_course(request, id):
    id = int(id)
    try:
        userid = Course.objects.get(id=id)
    except Course.DoesNotExist:
        return redirect('update_course')
    update = CourseForm(request.POST or None, id)
    if update.is_valid():
        update.save()
    return render(request, "update_user.html", {"update": update})


