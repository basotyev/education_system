from django.db import models


# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)


class Role(models.Model):
    role_name = models.CharField(max_length=32)


class User(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=64)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)


class Lesson(models.Model):
    content = models.JSONField()
    is_done = models.Value


class Course(models.Model):
    course_name = models.CharField(max_length=256)
    course_description = models.TextField()


class Course_lessons(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)


class Enrolled_course(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
