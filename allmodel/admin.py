from django.contrib import admin
from .client import Client
from .company import Company
from .product import Product
from .purchase import Purchase

admin.site.register(Client)
admin.site.register(Company)
admin.site.register(Purchase)
# Register your models here.
