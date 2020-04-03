from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'dashboard/base.html')

def client_form(request):
    return render(request,'dashboard/client_form.html')
