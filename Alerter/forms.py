from django import forms
from .models import *

# {#
# class StudentForm(forms.ModelForm):
# 	class Meta:
# 		model = Student
# 		fields = ['fName','lName', 'email']#}

class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['course','title', 'desc', 'dead']
