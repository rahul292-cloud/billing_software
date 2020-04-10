from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index' ),
    path('register',views.RegisterPage.as_view(), {'register': ''}, name='register' ),
    path('login',views.LoginPage.as_view(), {'login': ''}, name='login'),
    path('logout',views.logoutUser, name='logout' ),
    path('user/', views.userPage, name="user-page"),
<<<<<<< HEAD
=======
    path('account/', views.accountSettings, name="account"),

>>>>>>> eed9d4fdfad5a936421be5c959cb7b7e2cfe5201
    path('client_form/', views.Client.as_view(), {'client_form': ''}, name="client_form"),
    path('client_view/', views.Client.as_view(), {'client_view': ''}, name="client_view"),
    path('client_edit_form/<int:object_id>', views.ClientEdit.as_view(), {'client_edit_form': ''},
         name="client_edit_form"),
    path('client_delete/<int:object_id>', views.ClientDelete.as_view(), {'client_delete': ''},
         name="client_delete"),
    path('vendor_form/', views.Vendor.as_view(), {'vendor_form': ''}, name="vendor_form"),
    path('vendor_view/', views.Vendor.as_view(), {'vendor_view': ''}, name="vendor_view"),
    path('vendor_edit_form/<int:object_id>', views.VendorEdit.as_view(), {'vendor_edit_form': ''},
         name="vendor_edit_form"),
    path('vendor_delete/<int:object_id>', views.VendorDelete.as_view(), {'vendor_delete': ''},
         name="vendor_delete"),
    path('tax_form', views.Tax.as_view(),{'tax_form':''},name='tax_form'),
    path('tax_view/', views.Tax.as_view(), {'tax_view': ''}, name="tax_view"),
    path('tax_edit_form/<int:object_id>', views.TaxEdit.as_view(), {'tax_edit_form': ''},
         name="tax_edit_form"),
    path('tax_delete/<int:object_id>', views.TaxDelete.as_view(), {'tax_delete': ''},
         name="tax_delete"),

    path('company_form/', views.Company.as_view(), {'company_form': ''}, name="company_form"),
    path('company_view/', views.Company.as_view(), {'company_view': ''}, name="company_view"),
    path('company_edit_form/<int:object_id>', views.CompanyEdit.as_view(), {'company_edit_form': ''},
         name="company_edit_form"),
    path('company_delete/<int:object_id>', views.CompanyDelete.as_view(), {'company_delete': ''},
         name="company_delete"),

    path('purchase_form/', views.Purchase.as_view(), {'purchase_form': ''}, name="purchase_form"),
    # path('company_view/', views.Company.as_view(), {'company_view': ''}, name="company_view"),
    # path('company_edit_form/<int:object_id>', views.CompanyEdit.as_view(), {'company_edit_form': ''},
    #      name="company_edit_form"),
    # path('company_delete/<int:object_id>', views.CompanyDelete.as_view(), {'company_delete': ''},
    #      name="company_delete"),

    path('purchase', views.purchase, name='purchase'),

]
