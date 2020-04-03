from django.contrib import admin
from .client import Client
from .company import Company
from .product import Product
from .vendor import Vendor
from .tax import  Tax

admin.site.register(Client)
admin.site.register(Company)
admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(Tax)
# Register your models here.
