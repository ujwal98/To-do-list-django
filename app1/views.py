from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import add
from .forms import todo_form


def home(request):
	if request.user.is_authenticated:
		tasks = add.objects.filter(user=request.user).order_by('id')
	else:
		tasks = add.objects.order_by('id')
	form = todo_form()
	context={'tasks':tasks,'form':form}
	return render(request,'app1/home.html',context)

def about(request):
	return render(request,'app1/about.html')

@require_POST
def addTodo(request):
	form = todo_form(request.POST)

	if form.is_valid():
		if request.user.is_authenticated:
			new_todo = add(user=request.user, task = request.POST['task'])
			new_todo.save()
		else:
			new_todo = add(user=Null, task = request.POST['task'])
			new_todo.save()

	return redirect('/')


def TodoComplete(request,Todo_id):
	todo = add.objects.get(pk=Todo_id)
	todo.delete()
	return redirect('/')

	