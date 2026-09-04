from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .models import Student
# Create your views here.
def std_list(request):
    tasks=Student.objects.all()
    return render(request,'std_list.html', {'students': tasks})

def add_std(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        course = request.POST.get('course')
        email = request.POST.get('email')
        age = request.POST.get('age')
        mob = request.POST.get('mob')
        if name and course and email and age and mob:
            # date =request.POST.get('date')
            Student.objects.create(name=name, course=course, email=email, age=age, mob=mob)
            return redirect (reverse('studentapp:std_list'))
        return render(request, 'add_std.html', {'error_msg': 'Please fill in all fields.'})
    return render(request, 'add_std.html')

def std_detail(request,id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'std_details.html', {'student': student})

def std_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect(reverse('studentapp:std_list'))
    return render(request, 'std_delete.html', {'student': student})

def std_edit(request, id):
    student= get_object_or_404(Student, id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        course = request.POST.get('course')
        email = request.POST.get('email')
        age = request.POST.get('age')
        mob = request.POST.get('mob')
        student.save()
        if name and course and email and age and mob:
            student.name=name
            student.course=course
            student.email=email
            student.age=age
            student.mob=mob
            student.save()
            return render(request, 'edit_success.html', {'student': student})
        return render(request, 'add_std.html', {'student': student})
    return render(request, 'add_std.html', {'student': student})
