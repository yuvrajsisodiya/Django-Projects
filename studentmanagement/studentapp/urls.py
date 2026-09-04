from django.contrib import admin
from django.urls import path
from . import views 
app_name = 'studentapp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.std_list,name='std_list'),
    path('add/',views.add_std,name='add_std'),
    path('student/<int:id>/',views.std_detail ,name='std_detail'),  
    path('student/<int:id>/delete/', views.std_delete, name='std_delete'),
    path('student/<int:id>/edit/', views.std_edit, name='std_edit'),
    
    
]