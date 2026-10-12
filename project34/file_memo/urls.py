from django.urls import path
from . import views
urlpatterns = [
    # local cache memorey
    # path('youtube/channels/', views.channel_list, name='channel_list'),   
    path('file/channels/', views.channel_list_file , name="channel_list"),
]