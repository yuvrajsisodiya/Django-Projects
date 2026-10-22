from rest_framework.routers import DefaultRouter
from django.urls import path , include
from .views import TeacherViewSet
# as container ya varible
router =  DefaultRouter()
router.register(r'teachers',TeacherViewSet , basename='teacher')
urlpatterns=[
    path('',include(router.urls)),

]