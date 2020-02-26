from django.urls import path, include
from accounts.views import SignUpView, LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [

    # Accounts
    path('signup', SignUpView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login')


]