from django.shortcuts import render , redirect ,get_object_or_404
# model ko impost
from .models import Post
# PostForm form.py se import
from .forms import PostForm
from django.core.paginator import Paginator

def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts , 2)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request , 'post_list.html' , {'page_obj':page_obj})

def post_create(request):
    form = PostForm()
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    
    return render(request , 'post_form.html' , {'form' : form})

def post_delete(request ,post_id):
    post = get_object_or_404(Post , id = post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'post_confirm_delete.html', {'post': post})
