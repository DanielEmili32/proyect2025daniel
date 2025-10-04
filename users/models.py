from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name

class DetailProduct(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="products",
        on_delete=models.PROTECT
    )
    description = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    def __str__(self):
        return f"{self.product.name} - {self.description}"
