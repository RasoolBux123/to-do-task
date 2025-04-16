from django.shortcuts import render , redirect

from .models import Task
from .forms import TaskForm
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    return render(request, 'index.html')   
def task_list(request):
     tasks = Task.objects.filter(user=request.user)  # only show user's tasks
    
     return render(request, 'task_list.html', {'tasks': tasks})

def  task_create(request):
      if request.method == 'POST':
       form = TaskForm(request.POST)
       if form.is_valid():
          tweet= form.save(commit=False)
          tweet.user = request.user
          tweet.save()
          return redirect('task_list')
      
      else: 
          
          form = TaskForm()
      return render(request, 'task_create.html', {'form': form})  
    
def task_edit(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
         task = form.save(commit=False)
         task.user = request.user
         task.save()
        return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_create.html', {'form': form, 'task': task})

def task_delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user= request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_delete.html', {'task': task})
         
            


