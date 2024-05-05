from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.models import User

from user_management.models import Profile

# Create your views here.

def homepage_test(request):
    return HttpResponse("hello from homepage")


def homepage(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    return render(
        request,
        "homepage/home.html",
        {
            "user": user,
            "profile": profile
        }
    )