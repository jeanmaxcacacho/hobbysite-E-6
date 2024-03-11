from django.db import models

# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        ProductType,
        null=True,
        on_delete=models.CASCADE
        )
    description = models.TextField()
    # https://stackoverflow.com/questions/23739030/restrict-django-floatfield-to-2-decimal-places
    # {{ value | floatformat:2 }} when I get around to making the templaes
    price = models.FloatField()


    def __str__(self):
        return f"{self.name} -- {self.product_type}"
