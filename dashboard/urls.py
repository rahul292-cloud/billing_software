"""billing_software URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index' ),
    path('client_form',views.client_form,name='client_form' ),
    path('vendor_form',views.vendor_form,name='vendor_form' ),
    path('tax_form',views.tax_form,name='tax_form' ),
    # path('company_view',views.company_view,name='company_view' ),
    path('company_form/', views.Company.as_view(), {'company_form': ''}, name="company_form"),
    path('company_view/', views.Company.as_view(), {'company_view': ''}, name="company_view"),
    path('company_edit_form/<int:object_id>', views.CompanyEdit.as_view(), {'company_edit_form': ''}, name="company_edit_form"),
    # path('company_update/<int:object_id>', views.Company.as_view(), {'company_update': ''}, name="company_update"),
]
