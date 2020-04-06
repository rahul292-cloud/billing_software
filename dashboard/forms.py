import os
from django import forms
from allmodel import purchase, company

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
