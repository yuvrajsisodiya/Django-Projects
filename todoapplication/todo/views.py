from django.shortcuts import render,redirect , get_object_or_404
from django.urls import reverse
from .models import Task
# Create your views here.
def task_show(request):
    task=Task.objects.all().order_by('-create_date')
    return render(request,'todo/task_show.html',{'tasks':task})

def add_task(request):
    if request.method=='POST':
        title=request.POST.get('title')
        discription=request.POST.get('description')
        if title and discription:
            task=Task.objects.create(title=title,description=discription)
            return redirect(reverse('todo:task_show'))
        return render(request,'todo/add_task.html',{'error_msg':'Please fill in all fields.'}) 
    return render(request,'todo/add_task.html')

def task_delete(request,pk ):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect(reverse('todo:task_show'))  
    return render(request, 'todo/confrom_del.html', {'task': task})
 
def task_toggle(request , pk):
    # task = Task.objects.get(id=id)
    task = get_object_or_404(Task , pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect(reverse('todo:task_show'))

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and description:
            task.title = title
            task.description = description
            task.save()
            return redirect(reverse('todo:task_show'))
        return render(request, 'todo/add_task.html', {'task': task})
    return render(request, 'todo/add_task.html', {'task': task})
