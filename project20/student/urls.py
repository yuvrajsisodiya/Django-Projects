from django.urls import path
from . import views 
urlpatterns=[
    path('',views.stdfrom ,name='stdfrom'),
    path('addstd/',views.addstd, name='addstd'),
    path('success/',views.success , name='success'),
]