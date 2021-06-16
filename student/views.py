import instance as instance
import notification as notification
from django.contrib.sites.models import Site
from django.http import HttpResponse
from django.views.generic import CreateView, TemplateView
from admin_api.models import Course, User
from .forms import EnrolleCourseForm, SimpleUserForm, NewSolutionForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, models
from django.contrib import messages
from django.db.models import signals
from django.contrib.auth.forms import AuthenticationForm
from django.dispatch import receiver
from django.db.models.signals import post_save
from notifications.signals import notify



# Create your views here.
from .models import SimpleUser, Homework


def index(request):
    return render(request, 'index.html')

def teacher(request):
    return render(request, 'teacher.html')


def python(request):
    return render(request, 'python.html')


def cpp(request):
    return render(request, 'cpp.html')



def cpplesson1(request):
    create = NewSolutionForm()
    if request.method == 'POST':
        create = NewSolutionForm(request.POST, request.FILES)
        if create.is_valid():
            create.save()
            sender = SimpleUser.objects.get(username=request.user)
            receiver = SimpleUser.objects.get(email='teacher@teacher.com')
            notify.send(sender, recipient=receiver, verb='New Homework!', description=request.POST.get('New Homework!'))
            return redirect('http://127.0.0.1:8000/team/cpp_lesson1')
        else:
            return HttpResponse('ERROR!')
    else:
        return render(request, "cpp_lesson1.html", {"create": create})


def pythonlesson1(request):
    create = NewSolutionForm()
    if request.method == 'POST':
        create = NewSolutionForm(request.POST, request.FILES)
        if create.is_valid():
            create.save()
            sender = SimpleUser.objects.get(username=request.user)
            receiver = SimpleUser.objects.get(email='teacher@teacher.com')
            notify.send(sender, recipient=receiver, verb='New Homework!', description=request.POST.get('New Homework!'))
            return redirect('http://127.0.0.1:8000/team/python_lesson1')
        else:
            return HttpResponse('ERROR!')
    else:
        return render(request, "python_lesson1.html", {"create": create})


def pythonlesson2(request):
    create = NewSolutionForm()
    if request.method == 'POST':
        create = NewSolutionForm(request.POST, request.FILES)
        if create.is_valid():
            create.save()
            sender = SimpleUser.objects.get(username=request.user)
            receiver = SimpleUser.objects.get(email='teacher@teacher.com')
            notify.send(sender, recipient=receiver, verb='New Homework!', description=request.POST.get('New Homework!'))
            return redirect('http://127.0.0.1:8000/team/python_lesson2')
        else:
            return HttpResponse('ERROR!')
    else:
        return render(request, "python_lesson2.html", {"create": create})


def teacher(request):
    all = Homework.objects.all()
    return render(request, "teacher.html", {"all": all})


def about(request):
    return render(request, 'about.html')


def team(request):
    return render(request, 'team.html')


def admin(request):
    return render(request, 'admin_panel.html')


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


def registerView(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("http://127.0.0.1:8000")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render(request=request, template_name="registration/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if username == 'admin':
                login(request, user)
                return redirect("http://127.0.0.1:8000/admin_panel")
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("http://127.0.0.1:8000")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form": form})


class ProfileView(TemplateView):
    template_name = "registration/user_page.html"

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))
