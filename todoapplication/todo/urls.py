from django.contrib import admin
from django.urls import path
from .import views
app_name='todo'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.task_show, name='task_show'),
    path('toggle/<int:pk>/',views.task_toggle, name="task_toggle"),
    path('add/',views.add_task , name='add_task'),
    path('edit/<int:pk>/',views.task_edit, name='task_edit'),
    path('delete/<int:pk>/',views.task_delete, name='task_delete'),
    
]


