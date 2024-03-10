from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from .models import GuitarModel
from .mixins import SuperuserRequiredMixin

def home_view(request):
    return render(request, 'main/home.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)

            #Set password
            user.set_password(user_form.cleaned_data['password'])

            user.save()
            return render(request,
                          'main/register_done.html',
                          {'new_user': user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                'main/register.html',
                {'user_form': user_form})


class ListGuitarsView(ListView):
    model = GuitarModel

class CreateGuitarView(SuperuserRequiredMixin, CreateView):
    model = GuitarModel
    fields = '__all__'
    success_url=reverse_lazy('main:guitar_list')

