from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import ProductType, Product

# Create your views here.


def hello_test(request):
    return render(request, 'merchstore/hello.html')


class ItemList(ListView):
    """
    kekekekkekekekke
    """
    template_name = 'merchstore/itemlist.html'
    model = ProductType


class ItemDetail(DetailView):
    """
    LMALMAOLMAOMLALMALLMDASLDMALS
    """
    template_name = 'merchstore/itemdetail.html'
    model = Product
