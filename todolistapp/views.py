from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import Todolist
from .forms import Taskfom
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.

def todolist(request):
    if request.method == 'POST':
        form = Taskfom(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, "new task added")
        return redirect('todolist')
    else:

        tasks = Todolist.objects.all()
        pagination = Paginator(tasks, 7)
        page= request.GET.get('page')
        tasks= pagination.get_page(page)
        return render(request, 'todolist.html', {'alltask': tasks})



def delete_task(request, task_id):
    task = Todolist.objects.get(pk=task_id)
    task.delete()
    messages.info(request, "task has deleted successfully")
    return redirect('todolist')


def change_status(request, task_id):
    task= Todolist.objects.get(pk=task_id)
    if task.done :
        task.done=False
    else:
        task.done=True
    task.save()
    messages.success(request, "task status changed successfully")
    return redirect("todolist")


def edit_task(request, task_id):
    if request.method== 'POST':
       task= Todolist.objects.get(pk=task_id)
       form = Taskfom(request.POST or None , instance = task)
       if form.is_valid():
           form.save()
       messages.success(request, "task edited successfully")
       return redirect( 'todolist')
    else:
        etask= Todolist.objects.get(pk=task_id)
        return render(request, 'edit.html', {'etask': etask})




def contact(request):
    welcome_contact="welcome to the contact form!"
    return render(request, 'contact.html', {'welcome_contact':welcome_contact})

def about(request):
    welcome_about="welcome to about us form!"
    return render(request, 'about.html', {'welcome_about':welcome_about})

def index(request):
    welcome_index= "welcome to index page!"
    return render(request, 'index.html', {'welcome_index': welcome_index})