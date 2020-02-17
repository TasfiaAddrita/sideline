from django.urls import path, include
from .views import HobbiesDetailView, HobbiesListView, HobbiesEditView

urlpatterns = [
    path('', HobbiesListView.as_view(), name='hobbies-list'),
    path('<str:slug>', HobbiesDetailView.as_view(), name='hobbies-detail'),
    path('<str:slug>/edit', HobbiesEditView.as_view(), name='hobbies-edit')
]
