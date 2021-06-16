from django.forms import ModelForm, TextInput
from admin_api.models import Enrolled_course
from student.models import SimpleUser, Homework
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        User = get_user_model()
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class EnrolleCourseForm(ModelForm):
    class Meta:
        model = Enrolled_course
        fields = ['user_id', 'course_id']
        widgets = {
            'user_id': TextInput(attrs={
                'placeholder': "user id"
            }),
            'course_id': TextInput(attrs={
                'placeholder': "course id"
            })
        }


class SimpleUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = SimpleUser
        fields = ('first_name', 'last_name', 'email', 'username')


class NewSolutionForm(ModelForm):
    class Meta:
        model = Homework
        fields = ('username', 'lesson', 'solution')

    def save(self, commit=True):
        hw = super(NewSolutionForm, self).save(commit=False)
        if commit:
            hw.save()
        return hw

