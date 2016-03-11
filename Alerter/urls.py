from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^index/', views.index, name = "index"),
	url(r'^addstudent/', views.addStudent, name = "addStudent"),
	url(r'^addtask/', views.addTask, name = "addTask"),
	url(r'^login/', auth_views.login, name = "login"),
	#url(r'^login/$', 'example.views.login_user'),
]