from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import ProductType, Product

# Create your views here.

# List View: /merchstore/items
# Detail View: /merchstore/item/1

"""
So I'm guessing that the page /merchstore/items will list down all product types,
then per product type it will list down all the products that are in it.

Then all those product bullets are links to itemdetail.html probs.
"""

def hello_test(request):
    return render(request, 'merchstore/hello.html')


class ItemList(ListView):
    template_name = 'merchstore/itemlist.html'
    context_object_name = 'product_types'
    queryset = ProductType.objects.prefetch_related('products')


class ItemDetail(DetailView):
    model = Product
    template_name = 'merchstore/itemdetail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'
