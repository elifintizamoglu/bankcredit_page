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

def bank_a_application(request,slug):
    bank=BankOption.objects.get(name="Bank A")
    credit = get_object_or_404(Credit,slug=slug)        

    if request.method =='POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            customer= Customer(first_name=form.cleaned_data['first_name'],
                               last_name=form.cleaned_data['last_name'],
                               identification_number=form.cleaned_data['identification_number'],
                               job_title=form.cleaned_data['job_title'],
                               salary=form.cleaned_data['salary'],
                               bank=bank,
                               credit=credit)
            address_form = Address(district=form.cleaned_data['district'],
                               city=form.cleaned_data['city'])
                
            def customer_control(customer,address_form):
                flag= False
                try:
                    cstr_db=Customer.objects.get(identification_number=customer.identification_number)
                except:
                    try:
                        addr_db=Address.objects.get(district=address_form.district,
                                   city = address_form.city)
                        address_form.id=addr_db.id
                    except:
                        address_form.save()
                    finally:
                        customer.address=address_form
                        customer.save()
                        flag=True
                return flag
            
            if ((credit.slug == "mortgage-loan") and (customer.salary >= 50000)) or ((credit.slug == "car-loan") and (customer.salary >= 30000)) or ((credit.slug == "educational-loan") and (customer.salary >= 5000)):
                flag = customer_control(customer,address_form)
                return render(request,"credit/application-succesful.html", {"customer":customer}) if flag == True else render(request,"credit/application-done-before.html", {"customer":customer})
            else: 
                return render(request, "credit/application-failed.html")
            
        return render(request, "credit/application-form.html",{"form":form,"bank":bank,"credit":credit})
        
    else:
        form = ApplicationForm()
        return render(request, "credit/application-form.html",{"form":form,"bank":bank,"credit":credit})
    
def bank_b_application(request,slug):
    bank=BankOption.objects.get(name="Bank B")
    credit = get_object_or_404(Credit,slug=slug)

    if request.method =='POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            customer= Customer(first_name=form.cleaned_data['first_name'],
                               last_name=form.cleaned_data['last_name'],
                               identification_number=form.cleaned_data['identification_number'],
                               job_title=form.cleaned_data['job_title'],
                               salary=form.cleaned_data['salary'],
                               bank=bank,
                               credit=credit)
            address_form = Address(district=form.cleaned_data['district'],
                               city=form.cleaned_data['city'])
            
            def customer_control(customer,address_form):
                flag= False
                try:
                    cstr_db=Customer.objects.get(identification_number=customer.identification_number)
                except:
                    try:
                        addr_db=Address.objects.get(district=address_form.district,
                                   city = address_form.city)
                        address_form.id=addr_db.id
                    except:
                        address_form.save()
                    finally:
                        customer.address=address_form
                        customer.save()
                        flag=True
                return flag

            if ((credit.slug == "mortgage-loan") and (customer.salary >= 30000)) or ((credit.slug == "car-loan") and (customer.salary >= 10000)) or ((credit.slug == "educational-loan") and (customer.salary >= 3000)):
                flag = customer_control(customer,address_form)
                return render(request,"credit/application-succesful.html", {"customer":customer}) if flag == True else render(request,"credit/application-done-before.html", {"customer":customer})
            else: 
                return render(request, "credit/application-failed.html")         
                    
        return render(request, "credit/application-form.html",{"form":form,"bank":bank,"credit":credit})
        
    else:
        form = ApplicationForm()
        return render(request, "credit/application-form.html",{"form":form,"bank":bank,"credit":credit})
    
def bank_c_application(request,slug):
    bank=BankOption.objects.get(name="Bank C")
    credit = get_object_or_404(Credit,slug=slug)

    if request.method =='POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            customer= Customer(first_name=form.cleaned_data['first_name'],
                               last_name=form.cleaned_data['last_name'],
                               identification_number=form.cleaned_data['identification_number'],
                               job_title=form.cleaned_data['job_title'],
                               salary=form.cleaned_data['salary'],
                               bank=bank,
                               credit=credit)
            address_form = Address(district=form.cleaned_data['district'],
                               city=form.cleaned_data['city'])

            def customer_control(customer,address_form):
                flag= False
                try:
                    cstr_db=Customer.objects.get(identification_number=customer.identification_number)
                except:
                    try:
                        addr_db=Address.objects.get(district=address_form.district,
                                   city = address_form.city)
                        address_form.id=addr_db.id
                    except:
                        address_form.save()
                    finally:
                        customer.address=address_form
                        customer.save()
                        flag=True
                return flag


            if ((credit.slug == "mortgage-loan") and (customer.salary >= 25000)) or ((credit.slug == "car-loan") and (customer.salary >= 5000)) or ((credit.slug == "educational-loan") and (customer.salary >= 1000)):
                flag = customer_control(customer,address_form)
                return render(request,"credit/application-succesful.html",{"customer":customer}) if flag==True else render(request,"credit/application-done-before.html", {"customer":customer})
            else: 
                return render(request, "credit/application-failed.html")
        return render(request, "credit/application-form.html",{"form":form,"bank":bank,"credit":credit})
        
    else:
        form = ApplicationForm()
        return render(request, "credit/application-form.html",{"form":form,"bank":bank,"credit":credit})