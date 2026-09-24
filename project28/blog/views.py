from django.shortcuts import render
# Create your views here.
# function base view
# def post_list_view(request):
#     return render(request,'blog/post_list.html')
from .forms import PostForm
# class base view
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    # fields = ['title' , 'content']

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    # fields = ['title' , 'content']
    form_class = PostForm
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confrom_delete.html'
    success_url = '/'






