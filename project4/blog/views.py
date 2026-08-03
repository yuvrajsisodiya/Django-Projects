from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(req):
    return HttpResponse("<h1>home page from blog app</h1>")
def about(req):
    return HttpResponse("<h1>about page from blog app</h1>")
def contact(req):
    return HttpResponse("<h1>contact page from blog app</h1>")