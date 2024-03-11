from django.db import models

# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        )
    description = models.TextField()
    # https://stackoverflow.com/questions/23739030/restrict-django-floatfield-to-2-decimal-places
    # {{ value | floatformat:2 }} when I get around to making the templaes
    price = models.FloatField()
    
