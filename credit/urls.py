from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("credits",views.credits,name="credits-page"),
    path("credits/<slug:slug>", views.credit_detail, name="credit-detail-page") #/credits/credittype
]
