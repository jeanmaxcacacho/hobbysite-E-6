from django.db import models
from django.utils import timezone

from user_management.models import Profile

# Create your models here.

"""
FINALS SPECS

ProductType (same as midterms)
Product
 - the midterms fields (name, product type, description, price)
 - Owner (foreign key to Profile model, on delete model cascade)
 - stock (integer)
 - status (character field that can be: available [default], on sale, out of stock [when stock = 0])
Transaction
 - buyer (foreign key to profile, on delete null)
 - product (foreign key to product, on delete null)
 - amount (integer, amt of the Product bought)
 - status (character field taht can be: on cart, to pay, to ship, to receive, delivered)
 - created on (datetime, gets set when model is created)
"""

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return self.name

    
    class Meta:
        ordering = ['name']
    

class Product(models.Model):
    STATUS_CHOICES = (
        ('Available', 'Available'),
        ('On sale', 'On sale'),
        ('Out of stock', 'Out of stock')
    )

    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        ProductType,
        null=True,
        on_delete=models.SET_NULL,
        related_name='products'
        )
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    stock = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)    


    def __str__(self):
        return f"{self.name} -- {self.product_type} -- {self.owner.user.username}"


    class Meta:
        ordering = ['name']


class Transaction(models.Model):
    STATUS_CHOICES = (
        ('On cart', 'On cart'),
        ('To pay', 'To pay'),
        ('To ship', 'To ship'),
        ('To receive', 'To receive'),
        ('Delivered', 'Delivered')
    )

    buyer = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True
    )
    amount = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_on = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.product.name} -- {self.buyer.user.username} -- [TRANSACTION]"
