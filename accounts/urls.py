from django.urls import path, include
from accounts.views import SignUpView

urlpatterns = [

    # Accounts
    path('signup', SignUpView.as_view(), name='sign-up-page'),

]