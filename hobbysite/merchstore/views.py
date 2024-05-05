from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import ProductType, Product, Transaction
from .forms import TransactionForm, ProductForm, ProductUpdateForm

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
- user are not allowed to purchase their own products (we're gonna have an if user.is_authenticated view)
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
    template_name = "merchstore/product_list.html"
    context_object_name = 'product_types'
    queryset = ProductType.objects.prefetch_related('products')


class ProductDetailView(DetailView):
    model = Product
    template_name = "merchstore/product_detail.html"
    context_object_name = 'product'
    form_class = TransactionForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context

    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            product = self.get_object()
            transaction = form.save(commit=False)
            transaction.product = product
            transaction.buyer = request.user
            transaction.save()

            # udpating product stock
            product.stock -= transaction.quantity
            product.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

        
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            return redirect("merchstore:cart")
        else:
            return redirect(reverse_lazy("login"))

        
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "merchstore/product_create.html"
    success_url = reverse_lazy("merchstore:product_list")


    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)
    

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = "merchstore/product_update.html"
    success_url = reverse_lazy("merchstore:product_list")


    def form_valid(self, form):
        product = form.instance
        if product.stock == 0:
            product.status = 'Out of stock'
        else:
            product.status = 'Available'
        return super().form_valid(form)
    

class CartView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "merchstore/cart_view.html"
    context_object_name = "transactions"

    def get_queryset(self):
        return Transaction.objects.filter(buyer=self.request.user.profile)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transactions = context["transactions"]
        grouped_transactions = {}
        for transaction in transactions:
            owner = transaction.product.owner
            if owner not in grouped_transactions:
                grouped_transactions[owner] = []
            grouped_transactions[owner].append(transaction)
        context["grouped_transactions"] = grouped_transactions
        return context
    

class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "transaction_list.html"
    context_object_name = "transactions"

    def get_queryset(self):
        return Transaction.objects.filter(product__owner=self.request.user.profile)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transactions = context["transactions"]
        grouped_transactions = {}
        for transaction in transactions:
            buyer = transaction.buyer.user.username
            if buyer not in grouped_transactions:
                grouped_transactions[buyer] = []
            grouped_transactions[buyer].append(transaction)
        context["grouped_transactions"] = grouped_transactions
        return context