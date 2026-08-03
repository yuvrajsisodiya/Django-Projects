from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(req):
    return HttpResponse("home page from shop app")
def about(req):
    return HttpResponse("about page from shop app")
