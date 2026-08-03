from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def indx(request):
    # return HttpResponse("<h1 style='color:red'>Hello Django!</h1>")
    return HttpResponse("Hello Django?")
def about(request):
    return HttpResponse("Hello about page")
def add(resquest):
    a=2
    b=3
    return HttpResponse(f'addition is = {a+b}')    
def sub(request):
    a=22
    b=13
    return HttpResponse(f'subtration is = {a-b}')    