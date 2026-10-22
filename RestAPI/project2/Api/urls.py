from django.urls import path
from .views import StudentListView

urlpatterns = [
    path('students/', StudentListView.as_view(), name="students_list"),
    path('students/<int:id>/', StudentListView.as_view(), name="update-retrieve"),
]