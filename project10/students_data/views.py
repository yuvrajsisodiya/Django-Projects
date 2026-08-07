from django.shortcuts import render

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
class item:
    def __init__(self,I_name,I_price,I_rating):
        self.I_name=name,
        self.I_price=price,
        self.I_rating=I_rating,


def items_details(request):
    # i1=item('laptop',21999,4.2)
    data={
        'I_image':'https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/msft-echo-Surface-Laptop-Business-13.8-15-inch-device-flibbable-card-1?scl=1&fmt=png-alpha',
        'I_name':'HP Laptop',
        'I_price':21999,
        'I_rating':4,
    }

    return render(request,'students_data/student.html',data)