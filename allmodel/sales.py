from .models import BaseModel
from django.db import models
from .vendor import Vendor


class Sales(BaseModel):
    sales_invoice = models.CharField(max_length=10, null=False, blank=False, editable=True)
    vendor_name = models.ForeignKey(Vendor, on_delete=models.CASCADE,null=True,blank=True)
    sales_date = models.DateTimeField(auto_now=True, null=False, blank=False)
    Final_Amount = models.DecimalField(max_digits=7, decimal_places=2,null=True,blank=True)

    def __str__(self):
        return self.sales_invoice

