from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new_search', views.search, name='search'),
]




