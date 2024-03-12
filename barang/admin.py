from django.contrib import admin
from barang.models import (Contact, Product, Brand, Category, ProductPicture)

# Register your models here.
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProductPicture)