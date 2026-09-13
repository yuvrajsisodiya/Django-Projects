from django.shortcuts import render , get_object_or_404 , redirect
from .forms import emp_form
from .models import Employe
def emp_list(request):
    employes = Employe.objects.all()
    return render(request, 'employe/emp_list.html', {'employes': employes})


def emp_create(request):
    form=emp_form()
    if request.method == 'POST':
        form = emp_form(request.POST)
        if form.is_valid():
            form.save()
            return render(request , 'employe/emp_success.html')
    return render(request ,'employe/emp_form.html',{'form':form})

def emp_details(request ,emp_id):
    employes = get_object_or_404(Employe , id = emp_id)
    return render(request, 'employe/emp_details.html', {'employe': employes})

def emp_delete(request, emp_id):
    employe = get_object_or_404(Employe , id = emp_id)
    if request.method == 'POST':
        employe.delete()
        return redirect('employe:emp_list')
    return render(request , 'employe/emp_delete.html',{'employe':employe})

def emp_update(request,emp_id):
    employe = get_object_or_404(Employe,id = emp_id)
    form = emp_form(instance=employe)
    if request.method == 'POST':
        form = emp_form( request.POST, instance=employe)
        if form.is_valid():
            form.save()
            return redirect('employe:emp_list')
    return render(request, 'employe/emp_form.html', {'form': form, 'employe': employe})