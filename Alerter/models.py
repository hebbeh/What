from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

# {#
# class Student(models.Model):
#     registered = models.OneToOneField(User, default="")
#     fName = models.CharField(max_length=200)
#     lName = models.CharField(max_length=200)
#     email = models.EmailField(max_length=200)

#     def __str__(self):
#         return self.fName #}

class Task(models.Model):
    student = models.ForeignKey(User)#, settings.AUTH_USER_MODEL)
    # student = models.OneToOneField(User)#, primary_key=True)
    course = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    dead = models.DateTimeField(default=timezone.now) 
    status = models.BooleanField(default=False)

    def publish(self):
        self.dead = timezone.now()
        self.save()

    def __str__(self):
        return self.title