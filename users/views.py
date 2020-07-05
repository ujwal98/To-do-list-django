from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import todo_form_new


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			txt = 'Account created for {username}!'
			messages.success(request, 'Your account has been created. Login now !!!')
			return redirect('login')
	else:
		form = UserCreationForm()		

	form = UserCreationForm()
	return render(request,'users/register.html', {'form':form})
	
@login_required
def profile(request):
	todo_list = Todo.objects.order_by('id')
	form = todo_form_new()
	context={'todo_list':todo_list,'form':form}
	return render(request,'users/profile.html',context)

@require_POST
def addTodo(request):
	form = todo_form_new(request.POST)

	if form.is_valid():
		new_todo = Todo(text = request.POST['text'])
		new_todo.save()

	return redirect('profile')


def TodoComplete(request,Todo_id):
	todo = Todo.objects.get(pk=Todo_id)
	todo.delete()
	return redirect('profile')	