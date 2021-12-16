from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreatingForm, CustomUserLoginForm
from django.contrib.auth import views as auth_views


class SignUpView(CreateView):
    form_class = CustomUserCreatingForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class LoginView(auth_views.LoginView):
    form_class = CustomUserLoginForm
    template_name = 'registration/login.html'



