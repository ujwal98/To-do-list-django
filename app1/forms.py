from django import forms

class todo_form(forms.Form):
	task = forms.CharField(max_length=30,
		widget=forms.TextInput(
			attrs={'placeholder':'Enter task to do'}))