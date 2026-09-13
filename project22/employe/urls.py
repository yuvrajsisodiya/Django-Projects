from django.urls import path
from . import views
app_name = 'employe'
urlpatterns = [
    path('', views.emp_create, name='emp_create'),
    path('emp_list/',views.emp_list , name='emp_list'),
     path('emp_details/<int:emp_id>/', views.emp_details, name='emp_details'),
     path('emp_delete/<int:emp_id>/' , views.emp_delete ,name='emp_delete'),
     path('emp_update/<int:emp_id>/',views.emp_update , name="emp_update"),

]