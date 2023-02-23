from django.shortcuts import render

from datetime import date

all_credits = [
    {
        "slug":"mortgage",
        "image":"birinci.png",
        "date":date(2023, 2, 23),
        "title": "Idunno",
        "excerpt": "What is happening!",
        "content":"111Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure, eos rem amet culpa harum repudiandae quae quam fugit soluta quo esse quos beatae neque, sapiente inventore. Saepe distinctio earum at." 
    },
    {
        "slug":"car",
        "image":"dorduncu.jpg",
        "date":date(2023, 5, 23),
        "title": "Idunno2",
        "excerpt": "What is happening!2",
        "content":"222Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure, eos rem amet culpa harum repudiandae quae quam fugit soluta quo esse quos beatae neque, sapiente inventore. Saepe distinctio earum at." 
    },
    {
        "slug":"business",
        "image":"ucuncu.png",
        "date":date(2023, 8, 23),
        "title": "Idunno3",
        "excerpt": "What is happening!3",
        "content":"333Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure, eos rem amet culpa harum repudiandae quae quam fugit soluta quo esse quos beatae neque, sapiente inventore. Saepe distinctio earum at." 
    }
]

def get_date(credit):
    return credit['date']

def starting_page(request):
    sorted_credits = sorted(all_credits, key=get_date)
    latest_credits= sorted_credits[-3:]
    return render(request, "credit/index.html", {"credits": latest_credits})

def credits(request):
    return render(request, "credit/all-credits.html", {"all_credits":all_credits})

def credit_detail(request,slug):
    identified_credit= next(credit for credit in all_credits if credit['slug']== slug)
    return render(request,"credit/credit-detail.html", {"credit":identified_credit})