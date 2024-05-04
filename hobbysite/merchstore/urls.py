"""
merchstore URLs
"""

from django.urls import path
from .views import ItemList, ItemDetail

# List View: /merchstore/items
# Detail View: /merchstore/item/1

app_name = 'merchstore'

urlpatterns = [
    path('items', ItemList.as_view(), name='item_list'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item_detail')
    ]

