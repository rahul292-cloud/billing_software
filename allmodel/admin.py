from django.contrib import admin
from .client import Client
from .company import Company
from .product import Product
from .vendor import Vendor
from .tax import  Tax
from .employee import Employee
from .sub_purchase import Sub_purchase_lines, Sub_purchase
from .purchase import Purchase

admin.site.register(Client)
admin.site.register(Company)
admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(Tax)
admin.site.register(Employee)
admin.site.register(Purchase)
# Register your models here.

class Sub_purchaseAdminInline(admin.TabularInline):
    model = Sub_purchase_lines
    fieldsets = [
        ('Sub_purchase Lines', {'fields': (
            ('product', 'product_name', 'product_code', 'qty', 'tax_per', 'unit_price'),
        )}),
    ]
    extra = 1

@admin.register(Sub_purchase)
class Sub_purchaseAdmin(admin.ModelAdmin):
    list_display = ['purchase', 'sub_total']
    list_filter = ['purchase', 'sub_total']
    search_fields = ['purchase', 'sub_total']
    inlines = [Sub_purchaseAdminInline]

    fieldsets = [
        ('Sub_purchase', {'fields': (
            ('purchase'),
            ('sub_total'),

        ), }),
    ]