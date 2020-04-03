from .models import BaseModel
from django.db import models


class Client(BaseModel):
     name=models.CharField(max_length=20,null=False,blank=False,editable=True)
     address=models.TextField(max_length=250,null=False,blank=False,editable=True)
     mobile_no=models.CharField(max_length=10,null=True,blank=True,editable=True)
     state=models.CharField(max_length=50,null=False,blank=False,editable=True)
     city=models.CharField(max_length=50,null=False,blank=False,editable=True)
     pin_no=models.IntegerField()

     def __str__(self):
         return self.name


