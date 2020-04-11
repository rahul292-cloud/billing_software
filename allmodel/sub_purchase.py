from .models import BaseModel
from django.db import  models
from .purchase import Purchase
from .product import Product
from.tax import Tax

class Sub_purchase(BaseModel):
    purchase=models.ForeignKey(Purchase,on_delete=models.CASCADE,null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    qty=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    product_name=models.CharField(max_length=250,null=True,blank=True,editable=True)
    product_code=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    unit_price = models.DecimalField(max_digits=7, decimal_places=2,null=True,blank=True)
    serial_no=models.CharField(max_length=500,null=True,blank=True,editable=True)
    tax_per=models.ForeignKey(Tax,on_delete=models.CASCADE,null=True,blank=True)
    amount=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    sub_total=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)

    def __str__(self):
        return self.purchase

    # @property
    # def net_salary(self):
    #     self.qty * self.unit_price
    #     return self.amount




