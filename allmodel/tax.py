from .models import  BaseModel
from django.db import models


class Tax(BaseModel):
    tax_name=models.CharField(max_length=20,null=False,blank=False,editable=True)
    tax_percentage=models.CharField(max_length=3,null=False,blank=False,editable=True)
    cgsct=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    sgsct=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    igsct=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)

    def __str__(self):
        return self.tax_name
