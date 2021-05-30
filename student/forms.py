from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput
from admin_api.models import Enrolled_course
from student.models import SimpleUser


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
        fields = ('first_name','last_name','email','username')