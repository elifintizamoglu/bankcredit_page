from django.shortcuts import render

def starting_page(request):
    return render(request, "credit/index.html")

def credits(request):
    return render(request, "credit/all-credits.html")

def credit_detail(request):
    pass