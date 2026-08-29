from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
def stdfrom(request):
    return render(request, 'stdfrom.html')

def addstd(request):
    if request.method=="POST":
        name=request.POST.get("name")
        age=request.POST.get("age")
        city=request.POST.get("city")
        email=request.POST.get("email")
        
        print(name, age, city, email)
        if name and age and city and email:
            Student.objects.create(
                name=name,
                age=age,
                city=city,
                email=email
            ) 
            return redirect("success")
        else:
             return HttpResponse("<h1>please enter all field data</h1>")
    return render(request,"stdfrom.html")

def success(request):
    return render(request,"success.html")