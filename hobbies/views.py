from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect

from .models import Hobbies
from .forms import HobbiesForm

class HobbiesListView(ListView):
    """Renders a list of all hobbies"""
    model = Hobbies

    def get(self, request):
        """ Returns a list of wiki pages. """
        hobbies = self.get_queryset().all()
        # published_time = self.get_queryset().all()[0].was_published_recently()
        return render(request, 'hobbies_list.html', {'hobbies': hobbies})

class HobbiesDetailView(DetailView):
    """Renders a specific hobby base on its slug"""
    model = Hobbies

    def get(self, request, slug):
        """ Returns a specific hobby page by slug """
        hobbies = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'hobbies_detail.html', {
          'hobbies': hobbies
        })

class HobbiesEditView(UpdateView):
    """Update a hobby's information"""
    model = Hobbies
    fields = '__all__'
    template_name = 'edit.html'

    def form_valid(self, form):
        hobbies = form.save()
        return redirect('hobbies-details', slug=hobbies.slug)

class HobbiesAddView(CreateView):
    """Add new hobby to the list"""
    model = Hobbies
    form_class = HobbiesForm
    template_name = 'hobbies-add.html'

    def post(self, request):
        form = HobbiesForm(request.POST)
        # form.instance.author = self.request.user
        if form.is_valid():
            hobbies = form.save()
            return redirect('hobbies-detail', slug=hobbies.slug)

def IndexView(request):
    template_name = "index.html"
    return render(request, template_name)