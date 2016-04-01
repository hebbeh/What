from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
	url(r'^index/', views.index, name = "index"),
	url(r'^indexTest/', views.indexTest, name = "indexTest"),
	url(r'^addstudent/', views.addStudent, name = "addStudent"),
	url(r'^addtask/', views.addTask, name = "addTask"),
	#url(r'^delete_new/$', views.delete_new, name = "delete_new"),
	url(r'^delete_new/(?P<id>\d+)/$', views.delete_new, name = "delete_new"),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
]