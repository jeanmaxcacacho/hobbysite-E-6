from django.shortcuts import render
from django.http import HttpResponse

from user_management.models import Profile

# Create your views here.

def homepage_test(request):
    return HttpResponse("hello from homepage")


def homepage(request):
    user = request.user
    profile = None
    if user.is_authenticated:
        profile = Profile.objects.filter(user=user).first()
    return render(
        request,
        "homepage/home.html",
        {
            "user": user,
            "profile": profile
        }
    )