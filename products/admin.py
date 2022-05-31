from django.contrib import admin

# Register your models here.

from .models import Product

# this is the site admin
admin.site.register(Product)