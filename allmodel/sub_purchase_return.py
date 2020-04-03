from .models import BaseModel
from django.db import models
from .purchase_return import Purchase_return
from .product import Product
from .tax import Tax


class Sub_purchase(BaseModel):
    purchase_return = models.ForeignKey(Purchase_return, on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True,blank=True)
    qty = models.DecimalField(max_digits=7, decimal_places=2,null=True,blank=True)
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    serial_no = models.CharField(max_length=500, null=True, blank=True, editable=True)
    tax_per = models.ForeignKey(Tax, on_delete=models.CASCADE,null=True,blank=True)
    amonut = models.DecimalField(max_digits=7, decimal_places=2,null=True,blank=True)
    sub_total = models.DecimalField(max_digits=7, decimal_places=2,null=True,blank=True)


