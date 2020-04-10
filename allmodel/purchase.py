from .models import BaseModel
from django.db import models
from .client import Client


class Purchase(BaseModel):
    purchase_invoice=models.CharField(max_length=10,null=False,blank=False,editable=True)
    purchase_date=models.DateTimeField(null=False,blank=False)
    client_name=models.ForeignKey(Client,on_delete=models.CASCADE,null=True,blank=True)
    purchase_address=models.CharField(max_length=10,null=False,blank=False,editable=True)
    reference_no=models.CharField(max_length=10,null=False,blank=False,editable=True)
    Final_Amount=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)

    def __str__(self):
        return self.purchase_invoice
