from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="app1-Home"),
    path('about/',views.about,name="app1-about"),  
    path('add/',views.addTodo,name="add")  ,
    path('complete/<Todo_id>',views.TodoComplete,name='complete')
    # path('deleteComplete/',views.deleteCompleted,name='delete')
]