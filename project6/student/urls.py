from django.urls import path,re_path
from . import views
urlpatterns=[
    path('',views.student,name='student'),
    path('welcome_user/<str:username>/',views.welcome_user,name="welcome_user"),
    path('student_detail/<int:std_id>/',views.student_detail,name="student_detail"),
    # mutliple variable add
    path('course_detail/<int:c_code>/<str:c_name>/',views.course_detail, name="course_detail"),
    re_path(r'^pass_year/(?P<year>[0-9]{4})/$',views.pass_year , name="pass_year"),
    path('cube/<int:radius>/',views.cube,name='cube'),
    
]