from .models import BaseModel
from django.db import models




class Product(BaseModel):
    product_code=models.CharField(max_length=125,null=False,blank=False,editable=True)
    name=models.CharField(max_length=500,null=False,blank=False)
    buy_price=models.DecimalField(max_digits=9,decimal_places=2,null=False,blank=False,editable=True)
    sell_price=models.DecimalField(max_digits=9,decimal_places=2,null=False,blank=False,editable=True)


    def __str__(self):
        return self.name[0:25]
