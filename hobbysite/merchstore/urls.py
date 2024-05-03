"""
merchstore URLs
"""

from django.urls import path
from .views import hello_test, ItemList, ItemDetail

# List View: /merchstore/items
# Detail View: /merchstore/item/1

urlpatterns = [
    path('hello', hello_test, name='hello_test'),
    path('items', ItemList.as_view(), name='item_list'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item_detail')
    ]

app_name = 'merchstore'
