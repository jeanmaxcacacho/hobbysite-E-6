from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage_test(request):
    return HttpResponse("hello from homepage")


@login_required
def homepage(request):
    return render(
        request,
        "",
        {

        }
    )