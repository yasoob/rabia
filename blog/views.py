from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import django
from django.conf import settings
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

def index(request):
    posts = Post.objects.order_by('-published_date')[:5]
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
    	form = CommentForm(request.POST)
    	if form.is_valid():
    		comment = form.save(commit=False)
    		comment.post = post
    		comment.save()
    		return redirect('blog.views.post_detail', pk=post.pk)
    else:
    	form = CommentForm()
    context = {'post': post,'form':form}
    return render(request, 'blog/post.html', context)

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog.views.post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog.views.post_detail', pk=post_pk)