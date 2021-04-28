from django.forms import ModelForm, TextInput
from admin_api.models import Enrolled_course


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
