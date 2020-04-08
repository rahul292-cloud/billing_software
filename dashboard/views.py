from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from allmodel import company
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group

# Create your views here.

class RegisterPage(View):
    register_template = "dashboard/register.html"

    @method_decorator(unauthenticated_user)
    def get(self, request, *args, **kwargs):
        if 'register' in kwargs:
            form = CreateUserForm()
            context = {'form': form}
            return render(request, self.register_template, context)

    def post(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request, 'Account was created for '+username)
            return redirect(to='login')

class LoginPage(View):
    login_template = "dashboard/login.html"

    @method_decorator(unauthenticated_user)
    def get(self, request, *args, **kwargs):

        if 'login' in kwargs:

            context = {}
            return render(request, self.login_template, context)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(to="index")
        else:
            messages.info(request, 'Username OR Password is incorrect')
            return render(request, self.login_template)

def logoutUser(request):
    logout(request)
    return redirect(to="login")

def userPage(request):
	context = {}
	return render(request, 'dashboard/user.html', context)

# @login_required(login_url='login')
class Company(View):
    form = CompanyForm
    model = company.Company
    companyForm_template = 'dashboard/company_form.html'
    companyView_template = 'dashboard/company_view.html'
    company_edit_Form_template = 'dashboard/company_form_edit.html'

    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['admin']))
    def get(self, request, *args, **kwargs):

        if 'company_form' in kwargs:
            return render(request, self.companyForm_template, {'form': self.form()})
        elif 'company_view' in kwargs:
            model= company.Company.objects.all()
            return render(request, self.companyView_template, {'form': model})


    def post(self, request, *args, **kwargs):
        form = self.form(request.POST, request.FILES)

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
            return redirect(to="company_view")

# @login_required(login_url='login')
class CompanyEdit(View):
    form = CompanyForm
    model = company.Company
    companyForm_template = 'dashboard/company_form.html'
    companyView_template = 'dashboard/company_view.html'
    company_edit_Form_template = 'dashboard/company_form_edit.html'

    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['admin']))
    def get(self, request, *args, **kwargs):
        if 'company_edit_form' in kwargs:
            record = self.model.objects.get(id=kwargs.get('object_id'))
            editForm = self.form(instance=record)
            return render(request, self.company_edit_Form_template, {'editForm': editForm})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST, request.FILES)

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
            self.model.objects.filter(pk=kwargs.get('object_id')).update(
                company_name=company_name, website_name=website_name, mobile_no=mobile_no, email_id=email_id,
                gst_in=gst_in, cin=cin, adress=adress, state=state, city=city, pin_no=pin_no
            )
            return redirect(to="company_view")

# @login_required(login_url='login')
class CompanyDelete(View):
    company_delete_template = 'dashboard/delete.html'
    model = company.Company

    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['admin']))
    def get(self, request, *args, **kwargs):
        if 'company_delete' in kwargs:
            item = self.model.objects.get(id=kwargs.get("object_id"))
            return render(request, self.company_delete_template, {'item':item})
    def post(self, request, *args, **kwargs):
        item = self.model.objects.get(id=kwargs.get("object_id"))
        item.delete()
        return redirect(to="company_view")




# def company_view(request):
    # model=company.Company.objects.all()
#     return render(request,'dashboard/company_view.html')


@login_required(login_url='login')
@admin_only
def index(request):
    return render(request,'dashboard/base.html')

def client_form(request):
    return render(request,'dashboard/clent_form.html')

def vendor_form(request):
    return render(request,'dashboard/vendor_form.html')

def tax_form(request):
    return render(request,'dashboard/tax_form.html')
