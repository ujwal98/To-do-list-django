from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


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
