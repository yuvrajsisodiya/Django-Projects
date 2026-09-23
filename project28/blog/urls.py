from django.contrib import admin
from django.urls import path
# from .import views
from .views import PostListView , PostDetailView , PostCreateView , PostUpdateView , PostDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/create/', PostCreateView.as_view() , name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]