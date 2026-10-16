from django.urls import path
from . import views

urlpatterns = [
    path('students/',views.get_student , name='get_student'),
    path('add_student/',views.add_student , name='add_student'),
    path('update_student/<int:id>/',views.update_student , name='update_student'),
]