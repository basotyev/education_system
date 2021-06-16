from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class SimpleUser(AbstractUser):
    def __str__(self):
        return self.username


class Homework(models.Model):
    username = models.CharField(max_length=64)
    lesson = models.CharField(max_length=256)
    solution = models.CharField(max_length=256)