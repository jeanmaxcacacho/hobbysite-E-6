from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage_test(request):
    return HttpResponse("hello from homepage")