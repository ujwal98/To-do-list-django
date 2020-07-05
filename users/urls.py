from django.urls import path
from . import views

urlpatterns = [  
    path('add/',views.addTodo,name="add_new")  ,
    path('complete/<Todo_id>',views.TodoComplete,name='complete_new')
]