from itertools import product

from django.contrib import admin
from users.models import Product, DetailProduct
# Register your models here.

admin.site.register(Product)
admin.site.register(DetailProduct)