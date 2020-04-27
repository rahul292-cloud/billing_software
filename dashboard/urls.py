from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('',views.index,name='index' ),
    path('register',views.RegisterPage.as_view(), {'register': ''}, name='register' ),
    path('login',views.LoginPage.as_view(), {'login': ''}, name='login'),
    path('logout',views.logoutUser, name='logout' ),
    path('user/', views.userPage, name="user-page"),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="dashboard/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="dashboard/password_reset_sent.html"),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="dashboard/password_reset_form.html"),
     name="password_reset_confirm"),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="dashboard/password_reset_done.html"),
        name="password_reset_complete"),



    path('account/', views.accountSettings, name="account"),

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

    # path('purchase_form/', views.Purchase.as_view(), {'purchase_form': ''}, name="purchase_form"),
    # path('purchase_form/', views.PurchaseView.as_view(), {'purchase_form': ''}, name="purchase_form"),
    # path('company_edit_form/<int:object_id>', views.CompanyEdit.as_view(), {'company_edit_form': ''},
    #      name="company_edit_form"),
    # path('company_delete/<int:object_id>', views.CompanyDelete.as_view(), {'company_delete': ''},
    #      name="company_delete"),

    # path('purchase', views.purchase, name='purchase'),

]
