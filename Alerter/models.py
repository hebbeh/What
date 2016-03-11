from django.db import models
from django.utils import timezone

class Student(models.Model):
    fName = models.CharField(max_length=200)
    lName = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.fName

class Task(models.Model):
    user = models.ForeignKey(Student)
    course = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    dead = models.DateTimeField(default=timezone.now) 
    status = models.BooleanField(blank=False, null=False)

    def publish(self):
        self.dead = timezone.now()
        self.save()

    def __str__(self):
        return self.title

