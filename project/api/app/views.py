# env Modules
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from django.shortcuts import redirect


# My Modules
from user.models import *
from api.user.serializers import *
from api.permissions import IsAdminOrReadOnly, IsDevise, IsUserOrReadOnly
from user.utils import *


#(vewstes.ModelViewSet): list, create, retrieve, partical_update, destroy

class UserViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated, IsUserOrReadOnly, IsAdminOrReadOnly,]

  queryset = User.objects.all()
  serializer_class = UserSerializer
  filter_backends = (DjangoFilterBackend, SearchFilter) 
  filterset_fields = ('id', 'username')


class RegisterUser(DataMixin, CreateView):
  form_class = RegisterUser
  success_url = reverse_lazy('login')

  def get_context_data(self, *, object_list=None, **kwargs):
    context = super().get_context_data(**kwargs)
    c_def = self.get_user_context(title="Registration")
    return dict(list(context.items()) + list(c_def.items()))

  def form_valid(self, form):
    user = form.save()
    login(self.request, user)
    return redirect('home')


class LoginUser(DataMixin, LoginView):
  template_name = 'ProgrammingCategory/login.html'

  def get_user_context(self, *, object_list=None, **kwargs):
    context = super().get_context_data(**kwargs)
    c_def = self.get_user_context(title="Avtorisetion")
    return dict(list(context.items()) + list(c_def.items()))
  
  def get_success_url(self):
    return reverse_lazy('home')

  def logout_user(request):
    logout(request)
    return redirect('login')
