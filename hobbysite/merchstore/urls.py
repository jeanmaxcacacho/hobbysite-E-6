"""
ProductListView: /merchstore/items
ProductDetailView: /merchstore/item/<int:pk>
ProductCreateView: /merchstore/item/add
ProductUpdateView: /merchstore/item/<int:pk>/edit
CartView: /merchstore/cart
TransactionView: /merchstore/transactions
"""

from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView

# List View: /merchstore/items
# Detail View: /merchstore/item/1

app_name = 'merchstore'

urlpatterns = [
    path("items", ProductListView.as_view(), name='product_list'),
    path("item/<int:pk>/", ProductDetailView.as_view(), name='product_detail'),
    path("item/add", ProductCreateView.as_view(), name="product_create")
    ]

