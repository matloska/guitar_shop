from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import GuitarModel

def home_view(request):
    return render(request, 'main/base.html')

class ListGuitarsView(ListView):
    model = GuitarModel

class CreateGuitarView(CreateView):
    model = GuitarModel
    fields = '__all__'
    success_url=reverse_lazy('main:guitar_list')
    #../guitar_list