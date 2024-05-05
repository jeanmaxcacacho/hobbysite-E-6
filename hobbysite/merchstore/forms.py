from django import forms

from .models import Product, ProductType, Transaction

class TransactionForm():
    quantity = forms.IntegerField(min_value=1, label="quantity")

    class Meta:
        model = Transaction
        fields = ["quantity"]