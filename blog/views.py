from django.shortcuts import get_object_or_404, render, redirect
from blog.models import Post
from .forms import PostForm

# Create your views here.


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})


def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('blog')
    return render(request, 'post_confirm_delete.html', {'post': post})
