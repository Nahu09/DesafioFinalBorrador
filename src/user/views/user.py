from django.shortcuts import render
from django.views.generic import CreateView
from user.form import SignUpForm
from django.urls import reverse_lazy



# Create your views here.


class SignUp(CreateView):
    template_name = 'register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')