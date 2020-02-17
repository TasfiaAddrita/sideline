from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Hobbies

class HobbiesListView(ListView):
    """Renders a list of all hobbies"""
    model = Hobbies


    def get(self, request):
        """ Returns a list of wiki pages. """
        hobbies = self.get_queryset().all()
        # published_time = self.get_queryset().all()[0].was_published_recently()
        return render(request, 'hobbies_list.html', {'hobbies': hobbies})

class HobbiesDetailView(DetailView):
    model = Hobbies

    def get(self, request, slug):
        """ Returns a specific hobby page by slug """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'hobbies_detail.html', {'hobbies': hobbies})

class HobbiesEditView(UpdateView):
    """"""
    model = Hobbies
    fields = '__all__'
    template_name = 'edit.html'

    def form_valid(self, form):
        hobbies = form.save()
        return redirect('hobbies-details', slug=hobbies.slug)
