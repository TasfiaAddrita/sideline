from django.urls import path, include
from accounts.views import SignUpView, LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [

    # Accounts
    path('signup', SignUpView.as_view(), name='signup'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login')


]