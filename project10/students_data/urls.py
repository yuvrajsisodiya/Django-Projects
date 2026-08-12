from django.urls import path
from . import views
urlpatterns = [ 
    # path('', views.std_details, name='std_details')
    # path('',views.course_details,name="course data")
    # path('',views.items_details,name='items')
    path('',views.std_details, name='std_details')

]