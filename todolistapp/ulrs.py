
from django.urls import path, include
from . import views

urlpatterns = [

    path('',views.todolist, name='todolist'),
    path('delete/<int:task_id>', views.delete_task, name="delete_task"),
    path('status/<int:task_id>', views.change_status, name='change_status'),
    path('edit/<int:task_id>', views.edit_task, name='edit_task'),
]
