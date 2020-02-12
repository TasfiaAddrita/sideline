from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Hobbies

class HobbiesListView(ListView):
    """Renders a list of all hobbies"""
    model = Hobbies

class HobbiesDetailView(DetailView):
    model = Hobbies
