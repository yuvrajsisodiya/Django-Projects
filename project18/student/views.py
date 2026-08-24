from django.shortcuts import render

# Create your views here.
from . models import student
def home(request):
    students=student.objects.all()
    context={
        'student':students
    }
    return render(request , 'home.html' ,context)