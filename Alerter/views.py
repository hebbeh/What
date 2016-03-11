from django.shortcuts import render, redirect
from .forms import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
	return render(request, "Alerter/index.html", context=None)

def addStudent(request):
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			print("hejsan")
			return redirect('Alerter:index')
	else:
		form = StudentForm()
	return render(request, "Alerter/addStudent.html", context={'form':form,})

def addTask(request):
	if request.method == "POST":
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			print("hejsan")
			return redirect('Alerter:index')
	else:
		form = TaskForm()
	return render(request, "Alerter/addTask.html", context={'form':form,})

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/index/')
    return render_to_response('login.html', context_instance=RequestContext(request))

   