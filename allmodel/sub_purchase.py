from .models import BaseModel
from django.db import  models
from .purchase import Purchase
from .product import Product
from.tax import Tax

class Sub_purchase(BaseModel):
    purchase=models.ForeignKey(Purchase,on_delete=models.CASCADE,null=True,blank=True)

    sub_total=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)

    # def __str__(self):
    #     return self.purchase

    class Meta:
        db_table = 'sub_purchase'
        verbose_name_plural = 'Sub_purchase'

class Sub_purchase_lines(BaseModel):
    sub_purchase = models.ForeignKey(Sub_purchase, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    qty = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    product_name = models.CharField(max_length=250, null=True, blank=True, editable=True)
    product_code = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    unit_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    serial_no = models.CharField(max_length=500, null=True, blank=True, editable=True)
    tax_per = models.ForeignKey(Tax, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'sub_purchase_line'
        verbose_name_plural = 'Sub_purchase Line'

