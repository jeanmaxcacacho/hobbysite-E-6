from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import ProductType, Product

# Create your views here.

# List View: /merchstore/items
# Detail View: /merchstore/item/1

"""
ProductListView (DONE)
- list all products in the system regardless of status
- when logged in, products by the logged in user in a separate group and removed from all products list
 - so it's there's two lists if somebody is logged in
- there should be a link that leads to product creation (listing something in the store)

ProductDetailView  (what I'm working on rn)
- user are not allowed to purchase their own products (so I guess get the same query as the one in ProductListView)
- form rendered here that is attached to the transaction model
 - form should be handled by this view also
- product stock should change accordingly
- if not logged in and form is valid redirect to login, if logged in redirect to cart view
 - transactions are only saved if the user is authenticated
- if stock is 0 then buy button should not be clickable (apparently an HTML attribute)
- if current user is the owner then there should be an edit button will lead to update view

ProductCreateView
- All fields should be available
- product type and status should be a drop down
- accessible only to logged in users

ProductUpdateView
- allow updates of all fields except Owner
- when stock is 0 automatic out of stock otherwise it's available
- only accessible to logged in users

CartView
- shows all transactions made by the logged in user as the buyer
- categorized by product's owner, similar to ProdListView

TransactionListView
- all transactions as the seller
- categorized by buyer
- only accessible to logged in users
"""

class ProductListView(ListView):
    template_name = 'merchstore/product_list.html'
    context_object_name = 'product_types'
    queryset = ProductType.objects.prefetch_related('products')


class ItemDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'merchstore/itemdetail.html'
