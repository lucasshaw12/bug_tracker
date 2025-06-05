from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class UserIndexView(LoginRequiredMixin, ListView):
    model = User
    template_name = "user_index.html"
    context_object_name = "users"
    login_url = reverse_lazy("login")
