from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

class StudentListView(APIView):
    def get(self, request , id=None):
        if id is not None:
            try:
              student = Student.objects.get(id = id)
            except Student.DoesNotExit():
              return Responese({"error":"Student Not found"},status = 404)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        students = Student.objects.all()
        serializer = StudentSerializer(  students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self , request , id ):
        try:
           student  = Student.objects.get(id = id)
        except Student.DoesNotExist:
           return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self , request , id ):
        try:
            student = Student.objects.get()
        except Student.DoesNotExist:
            return Response({"error":"Student Not Found"}, status=404)
        student.delete()
        return Response(status=204)
           
