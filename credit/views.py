from django.shortcuts import render, get_object_or_404
from .models import Credit, Customer, Address

def starting_page(request):
    allcredits = Credit.objects.all().order_by("-loan_amount")[:3]
    return render(request, "credit/index.html", {"credits": allcredits})

def credits(request):
    all_credits = Credit.objects.all()
    return render(request, "credit/all-credits.html", {"all_credits":all_credits})

def credit_detail(request,slug):
    identified_credit = get_object_or_404(Credit,slug=slug)
    return render(request,"credit/credit-detail.html", {"credit":identified_credit,"credit_customers": identified_credit.customers.all()})