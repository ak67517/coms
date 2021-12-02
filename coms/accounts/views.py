from django.shortcuts import render
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
from accounts import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    #Once user has successfully submit their sign up form
    #redirect user to login page
    success_url = reverse_lazy("accounts:login")
    template_name = 'accounts/signup.html'