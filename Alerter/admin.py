from django.contrib import admin
from .models import Student
from .models import Task

#Make model visible at admin-page
admin.site.register(Student)
admin.site.register(Task)