from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm
from .models import Profile

class UserCreateView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "user_management/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        return redirect(self.success_url)
    

@login_required
def dashboard(request):
    profile = request.user.profile
    return render(
        request,
        "user_management/dashboard.html",
        {
            "profile": profile
        }
    )