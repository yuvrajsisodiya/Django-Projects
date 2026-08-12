from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'student/base.html')

def home(request):
    return render(request, 'student/home.html')

def about(request):
    return render(request, 'student/about.html')

def contact(request):
    return render(request, 'student/contact.html')

def navbar(request):
    return render(request, 'student/navbar.html')