from django.contrib import admin
from django.urls import path
from .import views
app_name='todo'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.task_show, name='task_show'),
    path('toggle/<int:id>/',views.task_toggle, name="task_toggle"),
    path('add/',views.task_created , name='task_created'),
    # path('update/',views.task_update, name='task_update'),
    # path('delete/',views.task_delete, name='task_delete'),
    
]


