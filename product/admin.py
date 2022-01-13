from django.contrib import admin

# Register your models here.
from product.models import Product, ProductReview

admin.site.register(Product)
admin.site.register(ProductReview)