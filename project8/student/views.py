from django.shortcuts import render

# Create your views here.
# basic variables
# def std_details(request):
#     return render(request,'student/home.html ',{'name':'yuvraj', 'age':20})

def std_details(request):
    data={
        'name':'Yuvraj Sisodiya',
        'enrol':'DX2411XX',
        'sec':'M-18',
        'sem':'v',
        'colloge':'Govt.Holker (Model Autonomous) Science Colloge Indore(M.P.)'
        

    }
    return render(request,'student/home.html',data)

