from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    password = forms.PasswordInput()
    firstname = forms.CharField(label='First Name', max_length=20)
    lastname = forms.CharField(label='Last Name', max_length=20)


    class Meta:
        model = User
        fields = ["firstname", "lastname", "username", "email", "password1", "password2"]