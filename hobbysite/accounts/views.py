from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm
from .models import Profile

# Create your views here.

class UserCreateView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        return redirect(self.success_url)

# this view is a placeholder for the dashboard, the dashboard page is what users will be brought to upon login
@login_required
def dashboard(request):
    profile = request.user.profile
    return render(
        request,
        "accounts/dashboard.html",
        {
            "profile": profile
        }
    )
