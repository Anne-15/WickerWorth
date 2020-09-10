from django.http import HttpResponse
from  django.template import loader
from django.shortcuts import render
from . import models
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request, 'homepage/index.html')

def search(request):
    new_search = request.POST.get('new_search')
    stuff_for_frontend = {
        'new_search':new_search,
    }
    results = Search.objects.filter(Q(name__icontains=new_search) | Q(description__icontains=new_search))
    return render(request, 'homepage/search.html', stuff_for_frontend)
