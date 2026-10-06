from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def set_cookie(request):
    response = HttpResponse("Set Cookies Successfully")
    response.set_cookie("user","Yuvraj")
    response.set_cookie("course","Python")
    return response

def get_cookie(request):
    username = request.COOKIES.get("user")
    course_name = request.COOKIES.get("course")
    res = HttpResponse(f"<h2>Get Cookies successfully</h2><h3>Username: {username} and course : {course_name}</h3>")
    return res 

def delete_cookie(request):
    response = HttpResponse("<h2>Cookies Deleted succesfully </h2>")
    # response.delete_cookie("user")
    response.delete_cookie("course")
    return response


