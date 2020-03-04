from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, View
from .forms import SignUpForm
from django.shortcuts import render, redirect, reverse


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {'form': AuthenticationForm})

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
 
        if user is not None:
            login(request, userobj)
        else:
            return render(request, 'login.html', {'form': AuthenticationForm})


    