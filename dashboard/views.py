from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group

<<<<<<< HEAD
from allmodel import company, vendor, client, tax,purchase,sub_purchase
=======
from allmodel import company, vendor, client, tax, employee
>>>>>>> eed9d4fdfad5a936421be5c959cb7b7e2cfe5201


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
        print("check")
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            emp = employee.Employee.objects.create(
                user=user
            )

            messages.success(request, 'Account was created for ' + username)
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
            messages.info(request, 'Username or Password is incorrect')
            return render(request, self.login_template)


def logoutUser(request):
    logout(request)
    return redirect(to="login")


<<<<<<< HEAD
=======
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
>>>>>>> eed9d4fdfad5a936421be5c959cb7b7e2cfe5201
def userPage(request):
    context = {}
    return render(request, 'dashboard/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
	emp = request.user.employee
	form = EmployeeForm(instance=emp)

	if request.method == 'POST':
		form = EmployeeForm(request.POST, request.FILES,instance=emp)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'dashboard/account_settings.html', context)



class Company(View):
    form = CompanyForm
    model = company.Company
    companyForm_template = 'dashboard/company_form.html'
    companyView_template = 'dashboard/company_view.html'
    company_edit_Form_template = 'dashboard/company_form_edit.html'

    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['admin', 'customer']))
    def get(self, request, *args, **kwargs):
        if 'company_form' in kwargs:
            return render(request, self.companyForm_template, {'form': self.form()})
        elif 'company_view' in kwargs:
            model = self.model.objects.all()
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


class CompanyEdit(View):
    form = CompanyForm
    model = company.Company
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


class CompanyDelete(View):
    company_delete_template = 'dashboard/company_delete.html'
    model = company.Company

    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['admin']))
    def get(self, request, *args, **kwargs):
        if 'company_delete' in kwargs:
            item = self.model.objects.get(id=kwargs.get("object_id"))
            return render(request, self.company_delete_template, {'item': item})

    def post(self, request, *args, **kwargs):
        item = self.model.objects.get(id=kwargs.get("object_id"))
        item.delete()
        return redirect(to="company_view")


class Vendor(View):
    form = VendorForm
    model = vendor.Vendor
    vendorFrom_templates = 'dashboard/vendor_form.html'
    vendorView_templates = 'dashboard/vendor_view.html'

    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['admin']))
    def get(self, request, *args, **kwargs):
        if 'vendor_form' in kwargs:
            return render(request, self.vendorFrom_templates, {'vendor': self.form()})
        elif 'vendor_view' in kwargs:
            model = vendor.Vendor.objects.all()
            return render(request, self.vendorView_templates, {'form': model})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            vendor_name = form.cleaned_data.get('name')
            vendor_address = form.cleaned_data.get('address')
            mobile_no = form.cleaned_data.get('mobile_no')
            state = form.cleaned_data.get('state')
            city = form.cleaned_data.get('city')
            pin_no = form.cleaned_data.get('pin_no')
            self.model.objects.create(
                name=vendor_name, address=vendor_address, mobile_no=mobile_no, state=state, city=city, pin_no=pin_no
            )
            return redirect(to='vendor_view')


@login_required(login_url='login')
@admin_only
def index(request):
    return render(request, 'dashboard/base.html')


class VendorEdit(View):
    form = VendorForm
    model = vendor.Vendor
    vendorEdit_templates = 'dashboard/vendor_edit.html'

    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['admin']))
    def get(self, request, *args, **kwargs):
        if 'vendor_edit_form' in kwargs:
            recored = self.model.objects.get(id=kwargs.get('object_id'))
            editform = self.form(instance=recored)
            return render(request, self.vendorEdit_templates, {'editForm': editform})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            vendor_name = form.cleaned_data.get('name')
            vendor_address = form.cleaned_data.get('address')
            mobile_no = form.cleaned_data.get('mobile_no')
            state = form.cleaned_data.get('state')
            city = form.cleaned_data.get('city')
            pin_no = form.cleaned_data.get('pin_no')
            self.model.objects.filter(pk=kwargs.get('object_id')).update(
                name=vendor_name, address=vendor_address, mobile_no=mobile_no, state=state, city=city, pin_no=pin_no
            )
            return redirect(to='vendor_view')


class VendorDelete(View):
    vendor_delete_templates = 'dashboard/vendor_delete.html'
    model = vendor.Vendor

    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['admin']))
    def get(self, request, *args, **kwargs):
        if 'vendor_delete' in kwargs:
            delete_form = self.model.objects.get(id=kwargs.get("object_id"))
            return render(request, self.vendor_delete_templates, {'item': delete_form})

    def post(self, request, *args, **kwargs):
        item = self.model.objects.get(id=kwargs.get("object_id"))
        item.delete()
        return redirect(to="vendor_view")


class Client(View):
    form = ClientForm
    model = client.Client
    clientForm_templates = 'dashboard/client_form.html'
    clientView_templates = 'dashboard/client_view.html'

    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['admin']))
    def get(self, request, *args, **kwargs):
        if 'client_form' in kwargs:
            return render(request, self.clientForm_templates, {'client': self.form()})
        elif 'client_view' in kwargs:
            model = self.model.objects.all()
            return render(request, self.clientView_templates, {'form': model})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            client_name = form.cleaned_data.get('name')
            client_address = form.cleaned_data.get('address')
            mobile_no = form.cleaned_data.get('mobile_no')
            state = form.cleaned_data.get('state')
            city = form.cleaned_data.get('city')
            pin_no = form.cleaned_data.get('pin_no')
            self.model.objects.create(
                name=client_name, address=client_address, mobile_no=mobile_no, state=state, city=city, pin_no=pin_no
            )
            return redirect(to='client_view')


class ClientEdit(View):
    form = ClientForm
    model = client.Client
    clientEdit_templates = 'dashboard/client_edit.html'

    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['admin']))
    def get(self, request, *args, **kwargs):
        if 'client_edit_form' in kwargs:
            recored = self.model.objects.get(id=kwargs.get('object_id'))
            editform = self.form(instance=recored)
            return render(request, self.clientEdit_templates, {'editForm': editform})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            vendor_name = form.cleaned_data.get('name')
            vendor_address = form.cleaned_data.get('address')
            mobile_no = form.cleaned_data.get('mobile_no')
            state = form.cleaned_data.get('state')
            city = form.cleaned_data.get('city')
            pin_no = form.cleaned_data.get('pin_no')
            self.model.objects.filter(pk=kwargs.get('object_id')).update(
                name=vendor_name, address=vendor_address, mobile_no=mobile_no, state=state, city=city, pin_no=pin_no
            )
            return redirect(to='client_view')


class ClientDelete(View):
    client_delete_templates = 'dashboard/client_delete.html'
    model = client.Client

    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['admin']))
    def get(self, request, *args, **kwargs):
        if 'client_delete' in kwargs:
            delete_form = self.model.objects.get(id=kwargs.get("object_id"))
            return render(request, self.client_delete_templates, {'item': delete_form})

    def post(self, request, *args, **kwargs):
        item = self.model.objects.get(id=kwargs.get("object_id"))
        item.delete()
        return redirect(to="client_view")


class Tax(View):
    form = TaxForm
    model = tax.Tax
    taxForm_templates = 'dashboard/tax_form.html'
    taxView_templates = 'dashboard/tax_view.html'

    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['admin']))
    def get(self, request, *args, **kwargs):
        if 'tax_form' in kwargs:
            return render(request, self.taxForm_templates, {'tax': self.form()})
        elif 'tax_view' in kwargs:
            model = self.model.objects.all()
            return render(request, self.taxView_templates, {'form': model})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            tax_name = form.cleaned_data.get('tax_name')
            tax_percentage = form.cleaned_data.get('tax_percentage')
            cgsct = form.cleaned_data.get('cgsct')
            sgsct = form.cleaned_data.get('sgsct')
            igsct = form.cleaned_data.get('igsct')
            self.model.objects.create(
                tax_name=tax_name, tax_percentage=tax_percentage, cgsct=cgsct, sgsct=sgsct, igsct=igsct
            )
            return redirect(to='tax_view')


class TaxEdit(View):
    form = TaxForm
    model = tax.Tax
    taxEdit_templates = 'dashboard/tax_edit.html'

    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['admin']))
    def get(self, request, *args, **kwargs):
        if 'tax_edit_form' in kwargs:
            recored = self.model.objects.get(id=kwargs.get('object_id'))
            editform = self.form(instance=recored)
            return render(request, self.taxEdit_templates, {'editForm': editform})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            tax_name = form.cleaned_data.get('tax_name')
            tax_percentage = form.cleaned_data.get('tax_percentage')
            cgsct = form.cleaned_data.get('cgsct')
            sgsct = form.cleaned_data.get('sgsct')
            igsct = form.cleaned_data.get('igsct')
            self.model.objects.filter(pk=kwargs.get('object_id')).update(
                tax_name=tax_name, tax_percentage=tax_percentage, cgsct=cgsct, sgsct=sgsct, igsct=igsct
            )
            return redirect(to='tax_view')


class TaxDelete(View):
    tax_delete_templates = 'dashboard/tax_delete.html'
    model = tax.Tax

    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['admin']))
    def get(self, request, *args, **kwargs):
        if 'tax_delete' in kwargs:
            delete_form = self.model.objects.get(id=kwargs.get("object_id"))
            return render(request, self.tax_delete_templates, {'item': delete_form})

    def post(self, request, *args, **kwargs):
        item = self.model.objects.get(id=kwargs.get("object_id"))
        item.delete()
        return redirect(to="tax_view")

class Purchase(View):
    form1=PurchaseForm
    form2=Sub_PurchaseForm
    model1=purchase.Purchase
    model2=sub_purchase.Sub_purchase
    purchaseForm_templates='dashboard/purchase_form.html'

    def get(self,request,*args,**kwargs):
        if'purchase_form' in kwargs:
            context={
                'purchase':self.form1(),'sub_purchase':self.form2()
            }
            return render(request,self.purchaseForm_templates,context)
    def post(self,request,*args,**kwargs):
        form1=self.form1(request.POST)
        form2=self.form2(request.POST)
        if self.form1.is_valid():
            purchase_invoice = form1.cleaned_data.get('purchase_invoice')
            client_name = form1.cleaned_data.get('client_name')
            purchase_date = form1.cleaned_data.get('purchase_date')
            purchase_address = form1.cleaned_data.get('purchase_address')
            reference_no = form1.cleaned_data.get('reference_no')
            Final_Amount = form1.cleaned_data.get('Final_Amount')
            self.model1.objects.create(
                purchase_invoice=purchase_invoice, client_name=client_name, purchase_date=purchase_date, purchase_address=purchase_address,
                reference_no=reference_no, Final_Amount=Final_Amount
            )
            return redirect(to=''
                               '')





def purchase(request):
    return render(request, 'dashboard/purchase_form.html')
