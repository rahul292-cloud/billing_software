import os
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from allmodel import company,vendor,client,tax,purchase,employee,sub_purchase
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

# class PurchaseForm(forms.ModelForm):
#     class Meta:
#         model=purchase.Purchase
#         fields=[
#             'purchase_invoice','client_name','purchase_date','purchase_address','reference_no','Final_Amount'
#         ]
#         widgets = {
#             'purchase_invoice': forms.TextInput(attrs={'class':'form-control'}),
#             'client_name':forms.TextInput(attrs={'class':'form-control'}),
#             'purchase_date':forms.TextInput(attrs={'class':'form-control'}),
#             'purchase_address':forms.TextInput(attrs={'class':'form-control'}),
#             'reference_no':forms.TextInput(attrs={'class':'form-control'}),
#             'Final_Amount':forms.TextInput(attrs={'class':'form-control'}),
#         }

# class Sub_PurchaseForm(forms.ModelForm):
#     class Meta:
#         model=sub_purchase.Sub_purchase
#         fields=[
#             'product_name','product_code','qty','unit_price','tax_per','amount','serial_no','sub_total'
#         ]
#         widgets = {
#             'product_name': forms.TextInput(attrs={'class':'form-control'}),
#             'product_code':forms.TextInput(attrs={'class':'form-control'}),
#             'qty':forms.TextInput(attrs={'class':'form-control','id':'qty'}),
#             'unit_price':forms.TextInput(attrs={'class':'form-control','id':'unit'}),
#             'tax_per':forms.TextInput(attrs={'class':'form-control'}),
#             'amount':forms.TextInput(attrs={'class':'form-control'}),
#             'serial_no':forms.TextInput(attrs={'class':'form-control'}),
#             'sub_total':forms.TextInput(attrs={'class':'form-control'}),
#             'tax_per':forms.Select(attrs={'class': 'form-control form-control-sm'}),
#         }
#
#         @property
#         def qty_unit(self):
#             return


class EmployeeForm(ModelForm):
    class Meta:
        model = employee.Employee
        fields = '__all__'
        exclude = ['user']
