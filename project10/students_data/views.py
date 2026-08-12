from django.shortcuts import render
from datetime import datetime
# Create your views here.
# def std_details(request):
#     data={
#         'id': 1,
#         'name': 'yuvraj sisodiya',
#         'age': 20,
#         'course': 'bca',
#         'city': 'indore ujjain'
#     }
#     return render(request, 'students_data/student.html',data)

# def std_details(request):
#     id=1
#     name='yuvraj'
#     age='19'
#     colloge='Govt.Holker Science colloge indore MP'
#     return render(request,'students_data/student.html',{"id":id,"name":name,"age":age, "colloge":colloge})

# def course_details(request):
#     subjects={
#         'C_name':'BCA',
#         'Dse':'Data Warehousing & Mining',
#         'Major':'Computer grapics',
#         'Vocational':'web desigening Techneques',
#         'Intership':'intership & projects',
        
#     }
    # return render(request,'students_data/student.html',subjects)

# class
# class item:
#     def __init__(self,I_name,I_price,I_rating):
#         self.I_name=name,
#         self.I_price=price,
#         self.I_rating=I_rating,


# def items_details(request):
#     # i1=item('laptop',21999,4.2)
#     data={
#         'I_image':'https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/msft-echo-Surface-Laptop-Business-13.8-15-inch-device-flibbable-card-1?scl=1&fmt=png-alpha',
#         'I_name':'hp laptop',
#         'I_price':21999,
#         'I_rating':4,
#     }

#     return render(request,'students_data/student.html',data)

def std_details(request):
    sub = ['math','physics','cemestry']
    a=12
    b=10
    c=a+b-a
    c=c*12
    data1= {
        'id': 1,
        'name': 'yuvraj sisodiya',
        'age': 20,
        'course': 'bca',
        'city': 'indore ujjain',
        'subjects' : sub,
        'marks':{'hindi':82,'english':54,'maths':65},
        'sum':c,
        'mysum':"",
        'intro':'hello i am yuvi i am software enginer',
        'msg': '<h3>hello i am heading 3.</h3>',
        
    }
    data2={
        'age':19,
        'marks':76,
        'sub':{'hindi':83,'english':63,}

    }

    data3={
        'tittle':'my first django project',
        'discription':'this is my first django project',
        "author":'xyz',
        # 'date':datetime.now(),
        'Date':datetime.now().date(),
        'Time':datetime.now().time(),
        'month':datetime.now().month,
        'tags':'django,python,html,css,js',

    },
    std_info={
        'name':'yuvraj',
        'age':20,
        'course':'bca',
        # 'subjects': ['math','physics','chemistry','hindi','english'],
        # 'subjects' : None,
        'marks':{'hindi':82,'english':54,'maths':65,'science':75,'social':80},
    }
    # return render(request,'students_data/student.html',data1)
    # return render(request,'students_data/home.html',data2)
    # return render(request,'students_data/home.html',data3)
    return render(request,'students_data/home.html',std_info)
    