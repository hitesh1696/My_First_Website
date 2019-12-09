from django.views import generic
from .models import brand
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return brand.objects.all()

class DetailView(generic.DetailView):
    model = brand
    template_name = 'music/details.html'
class AlbumCreate(CreateView):
    model = brand
    fields = ['brand']
class AlbumUpdate(UpdateView):
    model = brand
    fields = ['brand']
class AlbumDelete(DetailView):
    model = brand
    success_url = reverse_lazy('Music:index')
class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'
class Login(View):
    user = login
    template_name = 'music/login.html'

    

