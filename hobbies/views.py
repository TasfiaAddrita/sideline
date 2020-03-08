from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Hobbies


def home(request):
    context = {
        'hobbies': Hobbies.objects.all()
    }
    return render(request, 'hobbies/index.html', context)

class HobbiesListView(ListView):
    model = Hobbies
    template_name = 'hobbies/list.html'    #<app>/<model>_<viewtype>.html
    context_object_name = 'hobbies'
    ordering = ['-date_posted']

class HobbiesDetailView(DetailView):
    model = Hobbies

class HobbiesCreateView(LoginRequiredMixin, CreateView):
    model = Hobbies
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class HobbiesUpdateView(LoginRequiredMixin,  UserPassesTestMixin, UpdateView):
    model = Hobbies
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class HobbiesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Hobbies
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'hobbies/about.html', { 'title': 'About'})

def explore(request):
    return render(request, 'hobbies/explore.html', {'title': 'Explore'})

def get_sideline(request):
    return render(request, 'hobbies/get_sideline.html', {'title': 'Get Sideline'})

def pricing(request):
    return render(request, 'hobbies/pricing.html', {'title': 'Sideline Pricing'})

def locations(request):
    return render(request, 'hobbies/locations.html', {'title': 'locations'})