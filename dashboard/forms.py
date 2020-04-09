import os
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from allmodel import company,vendor,client,tax, employee
from django.forms import ModelForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CompanyForm(forms.ModelForm):
    class Meta:
        model = company.Company
        fields = [
            'company_name', 'website_name', 'mobile_no', 'email_id', 'gst_in', 'cin', 'adress', 'state', 'city', 'pin_no'
        ]

        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'website_name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'mobile_no': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'email_id': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'gst_in': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'cin': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'adress': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'state': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'city': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'pin_no': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        }


class VendorForm(forms.ModelForm):
    class Meta:
        model = vendor.Vendor
        fields=[
            'name','address','mobile_no','state','city','pin_no'
        ]


        widgets ={

            'name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'address': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'mobile_no': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'state': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'city': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'pin_no': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model=client.Client
        fields = [
            'name', 'address', 'mobile_no', 'state', 'city', 'pin_no'
        ]

        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'address': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'mobile_no': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'state': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'city': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'pin_no': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        }

class TaxForm(forms.ModelForm):
    class Meta:
        model = tax.Tax
        fields = [
            'tax_name', 'tax_percentage', 'cgsct', 'sgsct', 'igsct'
        ]

        widgets = {

            'tax_name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'tax_percentage': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'cgsct': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'sgsct': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'igsct': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        }

class EmployeeForm(ModelForm):
    class Meta:
        model = employee.Employee
        fields = '__all__'
        exclude = ['user']