from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAAdin(admin.ModelAdmin):
    list_display = ['title', 'price', 'availability', 'datetime_modified', ]

