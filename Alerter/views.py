from django.shortcuts import render, redirect
from .forms import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.views.generic.edit import DeleteView # this is the generic view

# Create your views here.
def index(request):
	tasks = Task.objects.all()
	return render(request, "Alerter/index.html", context={'tasks': tasks})

def addStudent(request):
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			form.registered = request.user
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
			instance = form.save(commit=False)
			instance.student = request.user
			instance.save()
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
    return render_to_response('registration/login.html', context_instance=RequestContext(request))


def indexTest(request):
  tasks = Task.objects.all()
  if request.method=='POST':
    selected_entry = Task.objects.get(pk=request.POST['Task'])
    selected_entry.delete()
  return render(request, "Alerter/indexTest.html", context={'tasks': tasks})

def logout_view(request):
    logout(request)
    # Redirect to a success page.

def delete_new(request,id):
    tasks = Task.objects.all()
    #+some code to check if New belongs to logged in user
    u = Task.objects.get(pk=id)
    u.delete()
    return render(request, "Alerter/index.html", context={'tasks': tasks})

# class PostitDelete(DeleteView):
#     model = Task
#                                             # redirect the user
#     template_name = 'delete_new.html'

