from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def set_session(request):
    request.session["user"]="Yuvraj sisodiya"
    request.session["course"]="Python full stack"
    return HttpResponse("<h1>Saved session set succesfully</h1>")

def get_session(request):
    username = request.session.get("user")
    c1 = request.session.get("course")
    return HttpResponse(f"<h1>Welcome {username}</h1> <p>Course: {c1}</p>")

# data delete 
def del_session(request):
    # del request.session["user"]
    request.session.flush()
    return HttpResponse("<h1>Session delete sucessfully</h1>")