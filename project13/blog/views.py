from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'blog/base.html')
    
def home(request):
    return render(request,'blog/home.html')

def about(request):
    return render(request,'blog/about.html')
