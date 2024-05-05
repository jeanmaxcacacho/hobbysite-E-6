from django import forms

from .models import Product, ProductType, Transaction

class TransactionForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1, label="quantity")

    class Meta:
        model = Transaction
        fields = ["quantity"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["product_type"].queryset = ProductType.objects.all()
        self.fields["owner"].widget = forms.HiddenInput()