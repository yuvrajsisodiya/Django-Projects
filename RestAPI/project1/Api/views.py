from django.shortcuts import render
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
# Create your views here.\

# decorator @api_view(['GET']) is used to specify that this view function will handle GET requests. It allows the function to be called when a GET request is made to the specified URL.


@api_view(['GET'])
def get_student(request):
    students = Student.objects.all() # database se data fetch karna
    serializer = StudentSerializer(students, many=True) # data ko serialize karna
    return Response(serializer.data) # serialized data ko response me bhejna .Then api return JSON formet me

@api_view(['POST'])
def add_student(request):
    serializers = StudentSerializer(data=request.data) # data ko serialize karna

    if serializers.is_valid(): # data valid hai ya nahi check karna
        serializers.save() # data ko save karna
        return Response(serializers.data , status=201) # serialized data ko response me bhejna
    return Response(serializers.errors , status=400) # agar data valid nahi hai to error message bhejna

@api_view(['PUT','PATCH'])
def update_student(request , id):
    try:
        student = Student.objects.get(id=id) # database se data fetch karna
    except Student.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND) # agar data exist nahi karta to 404 error bhejna
    if request.method == 'PUT':
        serializer = StudentSerializer(student , data=request.data) # data ko serialize karna
    if serializer.is_valid(): # data valid hai ya nahi check karna
        serializer.save() # data ko save karna
        return Response(serializer.data) # serialized data ko response me bhejna    
    return Response(serializer.errors , status=400) # agar data valid nahi hai to error message bhejna