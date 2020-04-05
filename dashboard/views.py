from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'dashboard/base.html')

def client_form(request):
    return render(request,'dashboard/client_form.html')

def vendor_form(request):
    return render(request,'dashboard/vendor_form.html')

def tax_form(request):
    return render(request,'dashboard/tax_form.html')

def company_form(request):
    return render(request,'dashboard/company_form.html')
