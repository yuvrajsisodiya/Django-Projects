from django.urls import path
from . import views
urlpatterns = [
    path('',views.std_create,name='std_create'),
]