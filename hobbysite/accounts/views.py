from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Profile
from .forms import ProfileForm

# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")
