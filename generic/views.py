from django.shortcuts import render, redirect
from django.http import HttpResponse
import django
from django.conf import settings
from .models import HomePage

def index(request):
    homepage = HomePage.objects.all()[0]
    context = {'homepage': homepage}
    return render(request, 'index.html', context=context)

def resume(request):
    resume_url = HomePage.objects.all()[0]
    if resume_url.resume:
        resume_url = resume_url.resume.url
    else:
        resume_url = 'generic.views.index'
    return redirect(resume_url)

def about_us(request):
    homepage = AboutUs.objects.all()[0]
    context = {'homepage': homepage}
    return render(request, 'index.html', context=context)