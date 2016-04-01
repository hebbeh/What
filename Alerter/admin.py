from django.contrib import admin
from .models import Task

#Make model visible at admin-page
admin.site.register(Task)