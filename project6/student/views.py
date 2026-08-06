from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def student(req):
    return HttpResponse("hello student !")

def welcome_user(req,username):
    return HttpResponse(f"<h1>Welcome : {username}!</h1>")
def student_detail(req,std_id):
    return HttpResponse(f"<h1>Student detail With ID : {std_id}</h1>")

def course_detail(req,**kwargs):
    c_code = kwargs.get("c_code")
    c_name = kwargs.get("c_name")
    
    return HttpResponse(f"<h1>Course Code : {c_code}<br>Course Name : {c_name}</h1>")
def pass_year(req,year):
    return HttpResponse(f"<h1>Passing Year : {year}</h1>")
def cube(req,radius):
    area=3.141*radius*radius
    return HttpResponse(f"area of circle is : {area}")    


