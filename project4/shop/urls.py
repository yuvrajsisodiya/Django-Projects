# seprate urls from blog app
from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home, name="shop-home"),
    path('about/',views.about, name="shop-about"),
]