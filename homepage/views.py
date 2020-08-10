from django.http import HttpResponse
from  django.template import loader
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'homepage/index.html')

def search(request):
    new_search = request.POST.get('new_search')
    print(new_search)
    stuff_for_frontend = {
        'new_search':new_search,
    }
    return render(request, 'homepage/search.html', stuff_for_frontend)
