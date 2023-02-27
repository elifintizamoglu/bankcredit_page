from django.shortcuts import render

from datetime import date

from .models import Credit

all_credits = [
    {
        "slug":"mortgage",
        "image":"mortgage.jpg",
        "date":date(2023, 2, 23),
        "title": "Mortgage",
        "excerpt": "Used to buy a home or to borrow money against the value of a home you already own.",
        "content":"A mortgage is an agreement between you and a lender that gives the lender the right to take your property if you fail to repay the money you've borrowed plus interest. Mortgage loans are used to buy a home or to borrow money against the value of a home you already own." 
    },
    {
        "slug":"carloans",
        "image":"carloans.jpg",
        "date":date(2023, 5, 23),
        "title": "Car Loans",
        "excerpt": "Used to buy a car or to borrow money against the value of a car you already own.",
        "content":"A car loan is an agreement between you and a lender that gives the lender the right to take your property if you fail to repay the money you've borrowed plus interest. Car loans are used to buy a car or to borrow money against the value of a car you already own." 
    },
    {
        "slug":"educationloans",
        "image":"educationalloans.png",
        "date":date(2023, 8, 23),
        "title": "Education Loans",
        "excerpt": "Used for educational purposes.",
        "content":"An educational loan is given to students in the purpose of helping education." 
    }
]

def get_date(credit):
    return credit['date']

def starting_page(request):
    allcredits = Credit.objects.all()
    return render(request, "credit/index.html", {"credits": allcredits})

def credits(request):
    allcredits = Credit.objects.all()
    return render(request, "credit/all-credits.html", {"allcredits":allcredits})

def credit_detail(request,slug):
    #identified_credit= next(credit for credit in all_credits if credit['slug']== slug)
    identified_credit = Credit.objects.get(slug=slug)
    return render(request,"credit/credit-detail.html", {"credit":identified_credit})