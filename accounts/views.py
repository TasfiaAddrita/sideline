from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from .forms import SignUpForm
from django.shortcuts import render, redirect, reverse


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



class LoginView(View):

    #Render Login view
    def get(self, request):
            return render(request, 'login.html', { 'form':  AuthenticationForm })

    