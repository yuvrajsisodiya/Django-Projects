from django.urls import path
from . import views

urlpatterns = [
    path('youtube/channels/', views.channel_list, name='channel_list'),
]