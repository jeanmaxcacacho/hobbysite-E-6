from django.shortcuts import render

# Create your views here.


def hello_test(request):
    return render(request, 'merchstore/hello.html')
