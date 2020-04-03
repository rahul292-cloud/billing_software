from .models import BaseModel
from django.db import models

class Company(BaseModel):
    company_name=models.CharField(max_length=50,null=False,blank=False,editable=True)
    website_name=models.URLField(max_length=36,null=True,blank=True,editable=True)
    mobile_no=models.CharField(max_length=10,null=True,blank=True,editable=True)
    email_id=models.EmailField(max_length=60,null=True,blank=True,editable=True)
    gst_in=models.CharField(max_length=60,null=True,blank=True,editable=True)
    cin=models.CharField(max_length=60,null=True,blank=True,editable=True)
    adress=models.TextField(max_length=250,null=False,blank=False,editable=True)
    state=models.CharField(max_length=50,null=False,blank=False,editable=True)
    city = models.CharField(max_length=50, null=False, blank=False, editable=True)
    pin_no = models.IntegerField()
    # company_logo=models.FileField()

    def __str__(self):
        return self.company_name

