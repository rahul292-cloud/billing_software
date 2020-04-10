from .models import BaseModel
from django.db import models
from django.contrib.auth.models import User

class Employee(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True,)
    join_date = models.DateField(null=True, blank=True)
    address = models.TextField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    pin_code = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    mobile_no = models.CharField(max_length=100, null=True, blank=True)
    email_id = models.CharField(max_length=100, null=True, blank=True)

    qualification = models.TextField(null=True, blank=True)
    JobType = (
        ("Part Time", "Part Time"),
        ("Full Time", "Full Time"),
        ("Internship", "Internship"),
    )
    type = models.CharField(max_length=50, choices=JobType, null=True, blank=True)
    job_profile = models.CharField(max_length=100, null=True, blank=True)
    job_description = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(default='profile1.jpg', null=True, blank=True)

