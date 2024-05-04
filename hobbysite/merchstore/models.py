from django.db import models
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
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        ProductType,
        null=True,
        on_delete=models.SET_NULL,
        related_name='products'
        )
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.name} -- {self.product_type}"


    class Meta:
        ordering = ['name']
