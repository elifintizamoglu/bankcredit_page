from django.views import View
from django.views.generic.edit import FormView
from django.shortcuts import render, get_object_or_404
from .models import Credit, Customer, Address, BankOption
from.forms import ApplicationForm

def starting_page(request):
    allbanks = BankOption.objects.all()
    return render(request, "credit/index.html", {"banks": allbanks})

def credits(request):
    all_credits = Credit.objects.all()
    return render(request, "credit/all-credits.html", {"all_credits":all_credits})

def credit_detail(request,slug):
    identified_credit = get_object_or_404(Credit,slug=slug)
    return render(request,"credit/credit-detail.html", {"credit":identified_credit})#"credit_customers": identified_credit.customers.all()

def banks(request):
    all_banks=BankOption.objects.all()
    return render(request, "credit/all-banks.html", {"all_banks":all_banks})

def bank_detail(request,slug):
    identified_bank= get_object_or_404(BankOption,slug=slug)
    return render(request,"credit/bank-detail.html", {"bank":identified_bank,"bank_credits": identified_bank.credit_types.all()})

"""
class ApplicationView(View):
    def get(self,request):
        #bank=BankOption.objects.filter(slug=slug1)
        #credit=bank.objects.filter(credit_types__slug=slug2)
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
                               district=form.cleaned_data['district'],
                               city=form.cleaned_data['city'],
                               postal_code=form.cleaned_data['postal_code'])
            address_form.save()
            customer.address=address_form
            customer.save()
            all_credits = Credit.objects.all()
            return render(request, "credit/all-credits.html",{"all_credits":all_credits})

        return render(request, "credit/application-form.html",{"form":form})
    
class BankA_ApplicationView(View):

    def get(self,request):
        form = ApplicationForm()
        return render(request, "credit/application-form.html",{"form":form})
    
    def post(self,request,slug):

        def form_validate_save():
            if form.is_valid():
                customer= Customer(first_name=form.cleaned_data['first_name'],
                               last_name=form.cleaned_data['last_name'],
                               identification_number=form.cleaned_data['identification_number'],
                               job_title=form.cleaned_data['job_title'],
                               salary=form.cleaned_data['salary'])
            
                address_form = Address(street=form.cleaned_data['street'],
                               district=form.cleaned_data['district'],
                               city=form.cleaned_data['city'],
                               postal_code=form.cleaned_data['postal_code'])
                address_form.save()
                customer.address=address_form
                customer.save()
                all_credits = Credit.objects.all()
                return render(request, "application-succesful.html")
            return render(request, "credit/application-form.html",{"form":form})
            
        credit = get_object_or_404(Credit,slug=slug)
        form = ApplicationForm(request.POST)

        if (credit.slug == "mortgage-loan") & (form.cleaned_data['salary']>100000):
            form_validate_save()
        elif credit.slug == "car-loan" & (form.cleaned_data['salary']>50000):
            form_validate_save()
        elif (credit.slug == "educational-loan") & (form.cleaned_data['salary']>5000):
            form_validate_save()
"""

def bank_a_application(request,slug):
    if request.method =='POST':
        credit = get_object_or_404(Credit,slug=slug)
        form = ApplicationForm(request.POST)

        if form.is_valid():
            customer= Customer(first_name=form.cleaned_data['first_name'],
                               last_name=form.cleaned_data['last_name'],
                               identification_number=form.cleaned_data['identification_number'],
                               job_title=form.cleaned_data['job_title'],
                               salary=form.cleaned_data['salary'])
            
            address_form = Address(street=form.cleaned_data['street'],
                               district=form.cleaned_data['district'],
                               city=form.cleaned_data['city'],
                               postal_code=form.cleaned_data['postal_code'])
            address_form.save()
            customer.address=address_form
            customer.save()

            if (credit.slug == "mortgage-loan") and (customer.salary >= 100.000):
                return render(request, "credit/application-succesful.html")
            
            elif (credit.slug == "car-loan") and (customer.salary > 50000):
                return render(request, "credit/application-succesful.html")
            
            elif (credit.slug == "educational-loan") and (customer.salary > 5000):
                return render(request, "credit/application-succesful.html")
            
            else: 
                return render(request, "credit/application-failed.html")
            
        return render(request, "credit/application-form.html",{"form":form})
        
    else:
        form = ApplicationForm()
        return render(request, "credit/application-form.html",{"form":form})