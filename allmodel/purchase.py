from .models import BaseModel
from django.db import models
from .client import Client


class Purchase(BaseModel):
    purchase_invoice=models.CharField(max_length=10,null=False,blank=False,editable=True)
    client_name=models.ForeignKey(Client,on_delete=models.CASCADE,null=True,blank=True)
    purchase_date=models.DateTimeField(auto_now=True,null=False,blank=False)
    Final_Amount=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
