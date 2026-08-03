# seprate urls from blog app
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home, name="blog-home"),
    path('about/',views.about,name="blog-about")
]