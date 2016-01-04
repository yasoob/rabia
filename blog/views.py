from django.shortcuts import render
from django.http import HttpResponse
import django
from django.conf import settings
from .models import Post

def index(request):
    posts = Post.objects.order_by('-published_date')[:5]
    context = {'posts': posts}
    return render(request, 'blog.html', context)