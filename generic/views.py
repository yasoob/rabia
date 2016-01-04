from django.shortcuts import render
from django.http import HttpResponse
import django
from django.conf import settings
from .models import HomePage

def index(request):
    homepage = HomePage.objects.all()[0]
    context = {'homepage': homepage}
    return render(request, 'index.html', context=context)