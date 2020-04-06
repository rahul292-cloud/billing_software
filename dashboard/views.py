from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .forms import *
from allmodel import company

# Create your views here.

class Company(View):
    form = CompanyForm
    model = company.Company

    companyForm_template = 'dashboard/company_form.html'

    def get(self, request, *args, **kwargs):
        if 'company_form' in kwargs:
            return render(request, self.companyForm_template, {'form': self.form()})
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST, request.FILES)
        # print(form.is_valid())
        if form.is_valid():
            company_name = form.cleaned_data.get('company_name')
            website_name = form.cleaned_data.get('website_name')
            mobile_no = form.cleaned_data.get('mobile_no')
            email_id = form.cleaned_data.get('email_id')
            gst_in = form.cleaned_data.get('gst_in')
            cin = form.cleaned_data.get('cin')
            adress = form.cleaned_data.get('adress')
            state = form.cleaned_data.get('state')
            city = form.cleaned_data.get('city')
            pin_no = form.cleaned_data.get('pin_no')
            self.model.objects.create(
                company_name=company_name, website_name=website_name, mobile_no=mobile_no, email_id=email_id,
                gst_in=gst_in, cin=cin, adress=adress, state=state, city=city, pin_no=pin_no
            )
            return redirect(to="company_form")


def company_view(request):
    model=company.Company.objects.all()
    return render(request,'dashboard/company_view.html',{'form':model})



def index(request):
    return render(request,'dashboard/base.html')

def client_form(request):
    return render(request,'dashboard/client_form.html')

def vendor_form(request):
    return render(request,'dashboard/vendor_form.html')

def tax_form(request):
    return render(request,'dashboard/tax_form.html')
