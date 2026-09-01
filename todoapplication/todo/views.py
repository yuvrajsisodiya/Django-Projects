from django.shortcuts import render,redirect , get_object_or_404
from django.urls import reverse
from .models import Task
# Create your views here.
def task_list(request):
    task=Task.objects.all().order_by('-create_date')
    return render(request,'todo/task_list.html',{'tasks':task})

def task_created(request):
    if request.method=='POST':
        title = request.POST.get('title','').strip()
        description = request.POST.get('description','').strip()
        if title:
            Task.objects.create(
                title=title,
                description=description
            )
            return redirect(reverse('todo:task_list'))
        error = "Title cannot be empty"
        return render(request,'todo/task_from.html',{'error':error})
    return render(request,'todo/task_from.html')

def task_update(request,pk):
    task=get_object_or_404(Task , pk=pk)
    if request.mothod =='POST':
        title = request.POST.get('title','').strip()
        description = request.POST.get('description','').strip()
        completed = request.POST.get('completed') =='on'

        if title:
            task.title = title
            task.description =  description
            task.completed = completed
            task.save()
            return redirect(reverse('todo:task_list'))
        return render(request,'todo/task_from.html',{'task':task})

def task_delete(reuquest):
    task = get_object_or_404(Task ,pk)
    if request.method == 'POST':
        task.delete()
        return redirect(reverse('todo:task_list'))
    return render(request,'todo/task_succes_delete.html',{'task':task})

def task_toggle(request,pk):
    task = get_object_or_404(Task , pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect(reverse('todo:task_list'))