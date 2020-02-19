from django.urls import path
from hobbies.views import HobbiesDetailView, HobbiesListView, HobbiesEditView, HobbiesAddView

urlpatterns = [
    path('', HobbiesListView.as_view(), name='hobbies-list'),
    path('<str:slug>', HobbiesDetailView.as_view(), name='hobbies-detail'),
    path('<str:slug>/edit', HobbiesEditView.as_view(), name='hobbies-edit'),
    path('add/', HobbiesAddView.as_view(), name='hobbies-add'),
]
