from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import Credit, Customer, Address
from.forms import ApplicationForm

def starting_page(request):
    allcredits = Credit.objects.all().order_by("-loan_amount")[:3]
    return render(request, "credit/index.html", {"credits": allcredits})

def credits(request):
    all_credits = Credit.objects.all()
    return render(request, "credit/all-credits.html", {"all_credits":all_credits})

def credit_detail(request,slug):
    identified_credit = get_object_or_404(Credit,slug=slug)
    return render(request,"credit/credit-detail.html", {"credit":identified_credit})#"credit_customers": identified_credit.customers.all()

"""
def banks(request):
    all_banks=Bank.objects.all()
    return render(request, "credit/all-banks.html", {"all_banks":all_banks})


def bank_detail(request,slug):
    identified_bank= get_object_or_404(Bank,slug=slug)
    return render(request,"credit/bank-detail.html", {"bank":identified_bank,"bank_credits": identified_bank.credit_types.all()})
"""
class ApplicationView(View):
    def get(self,request):
        form = ApplicationForm()
        return render(request, "credit/application-form.html",{"form":form})

    def post(self,request):
        form = ApplicationForm(request.POST)
    
        if form.is_valid():
            form.save()
            return render(request, "credit/all-credits.html")
        
        return render(request, "credit/application-form.html",{"form":form})
    


"""
def application_form(request):
    if request.method =='POST':
       form = ApplicationForm(request.POST)

       if form.is_valid():
            customer= Customer(first_name=form.cleaned_data['first_name'],
                               last_name=form.cleaned_data['last_name'],
                               identification_number=form.cleaned_data['identification_number'],
                               job_title=form.cleaned_data['job_title'],
                               salary=form.cleaned_data['salary'])
            
            address_form = Address(street=form.cleaned_data['street'],
                               building_name=form.cleaned_data['building_name'],
                               flat_no=form.cleaned_data['flat_no'],
                               district=form.cleaned_data['district'],
                               city=form.cleaned_data['city'],
                               postal_code=form.cleaned_data['postal_code'])
            address_form.save()
            customer.address=address_form
            customer.save()
            
            return render(request, "credit/all-credits.html")
       
    else:
        form = ApplicationForm()

    return render(request, "credit/application-form.html",{"form":form})
"""
"""
class ApplicationView(View):
    def get(self,request):
        form = ApplicationForm()

        return render(request, "credit/application-form.html",{"form":form})

    def post(self,request):
        form = ApplicationForm(request.POST)

        if form.is_valid():
            customer= Customer(first_name=form.cleaned_data['first_name'],
                               last_name=form.cleaned_data['last_name'],
                               identification_number=form.cleaned_data['identification_number'],
                               job_title=form.cleaned_data['job_title'],
                               salary=form.cleaned_data['salary'])
            
            address_form = Address(street=form.cleaned_data['street'],
                               building_name=form.cleaned_data['building_name'],
                               flat_no=form.cleaned_data['flat_no'],
                               district=form.cleaned_data['district'],
                               city=form.cleaned_data['city'],
                               postal_code=form.cleaned_data['postal_code'])
            address_form.save()
            customer.address=address_form
            customer.save()
            return render(request, "credit/all-credits.html")
        
    """
        
