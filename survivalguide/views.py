from __future__ import absolute_import
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import generic

from .forms import RegistrationForm

class HomePageView(generic.TemplateView):
    template_name = 'home.html'

class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    model = UserCreationForm
    template_name = 'accounts/signup.html'
