from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("credits",views.credits,name="credits-page"),
    path("credits/<slug:slug>", views.credit_detail, name="credit-detail-page"), #/credits credittype
    path("banks",views.banks,name="banks-page"),
    path("banks/<slug:slug>",views.bank_detail,name="bank-detail-page"),
    path("banks/bank-a/<slug:slug>",views.bank_a_application,name="bank-a-credit-application-page"),
    path("banks/bank-b/<slug:slug>",views.bank_b_application,name="bank-b-credit-application-page"),
    path("banks/bank-c/<slug:slug>",views.bank_c_application,name="bank-c-credit-application-page")  
]
