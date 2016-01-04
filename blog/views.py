from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import django
from django.conf import settings
from .models import Post

def index(request):
    posts = Post.objects.order_by('-published_date')[:5]
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(request, 'blog/post.html', context)