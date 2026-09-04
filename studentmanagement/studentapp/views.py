from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
# Create your views here.
def std_list(request):
    tasks=Student.objects.all()
    return render(request,'std_list.html', {'students': tasks})

def add_std(request):
    if request.method == 'POST':
        name = request.POST['name']
        course = request.POST['course']
        email = request.POST['email']
        age = request.POST['age']
        # date =request.POST['date']
        Student.objects.create(name=name, course=course, email=email, age=age)
        return redirect('studentapp:std_list')
    return render(request, 'add_std.html')

def std_detail(request,id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'std_details.html', {'student': student})
