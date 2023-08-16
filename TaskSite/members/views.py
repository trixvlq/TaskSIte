from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView
from .forms import *
from django.contrib.auth.models import User
class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration.html'
    success_url = reverse_lazy('Login')

class LoginUser(LoginView):
    form_class = ProfileForm
    template_name = 'login.html'
    success_url = "Task:HomePage"
@login_required
def logout_view(request):
    logout(request)
    return redirect("HomePage")