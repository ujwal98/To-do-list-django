from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import add
from .forms import todo_form


def home(request):
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
		new_todo = add(task = request.POST['task'])
		new_todo.save()

	return redirect('/')


def TodoComplete(request,Todo_id):
	todo = add.objects.get(pk=Todo_id)
	todo.delete()
	# todo.save()

	return redirect('/')

# def deleteCompleted(request):
# 	add.objects.filter(complete__exact=True).delete()

# 	return redirect('/')	