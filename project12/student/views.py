from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'student/base.html')

def home(request):
    return render(request,'student/home.html')

def about(request):
    students = [
    {'name': 'Yuvraj', 'dept': 'IT', 'fees': 50000, 'year': 2},
    {'name': 'Rahul', 'dept': 'IT', 'fees': 55000, 'year': 3},
    {'name': 'Aman', 'dept': 'BSC', 'fees': 45000, 'year': 2},
    {'name': 'Vikas', 'dept': 'CS', 'fees': 60000, 'year': 3},
    {'name': 'Priya', 'dept': 'BCA', 'fees': 40000, 'year': 1},
    {'name': 'Neha sharma', 'dept': 'BCA', 'fees': 50000, 'year': 2},
    {'name': 'Neha gupta', 'dept': 'Bcom', 'fees': 50000, 'year': 2},
    {'name': 'Mayank', 'dept': 'BCA', 'fees': 40000, 'year': 1},
     {'name': 'Chetna', 'dept': 'Bcom', 'fees': 40000, 'year': 1},
]
    return render(request,'student/about.html',{"students":students})
def std(request):
    std_list = [
    {'name': 'Yuvraj', 'dept': 'BCA', 'year': 2, 'fees': 50000},
    {'name': 'Rahul', 'dept': 'BCA', 'year': 2, 'fees': 55000},
    {'name': 'Priya', 'dept': 'BCA', 'year': 1, 'fees': 45000},
    {'name': 'Aman', 'dept': 'IT', 'year': 1, 'fees': 40000},
    {'name': 'Neha', 'dept': 'IT', 'year': 2, 'fees': 48000},
    {'name': 'Vikas', 'dept': 'CS', 'year': 3, 'fees': 60000},
    {'name': 'Ravi', 'dept': 'CS', 'year': 2, 'fees': 52000},
    ]

    std_marks=[
        {'name':'yuvraj', 'marks':68},
        {'name':'raj', 'marks':48},
        # {'name':'deepak', 'marks':58},
        # {'name':'mayank', 'marks':65},

    ]
    return render(request,'student/std.html',{'std_list':std_list, 'std_marks':std_marks})
