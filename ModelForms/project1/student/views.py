from django.shortcuts import render
from .form import stdform   

# Create your views here.
def std_create(request):
    form = stdform(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request,'std_success.html')
        
    return render(request,'std_form.html',{'form':stdform()})
