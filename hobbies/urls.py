from django.urls import path, include
from .views import HobbiesDetailView, HobbiesListView 

urlpatterns = [
    path('', HobbiesListView.as_view(), name='hobbies-home'),
    path('hobbies-detail/<int:pk>', HobbiesDetailView.as_view(), name='hobbies-detail'),
]