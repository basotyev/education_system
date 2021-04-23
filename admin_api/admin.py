from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Admin)
admin.site.register(User)
admin.site.register(Lesson)
admin.site.register(Course)
admin.site.register(Course_lessons)
admin.site.register(Enrolled_course)
admin.site.register(Role)

