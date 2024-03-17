from django.db import models
# Create your models here.

"""
so the procedure is going to be:
1. instantiate product types
2. instantiate product per product type
3. test the queries out in shell
4. setup the templates
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
