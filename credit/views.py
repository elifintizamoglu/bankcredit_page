from django.shortcuts import render

from datetime import date

credits = [
    {
        "slug":"mortgage",
        "image":"birinci.png",
        "date":date(2023, 2, 23),
        "title": "Idunno",
        "excerpt": "What is happening!",
        "content":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure, eos rem amet culpa harum repudiandae quae quam fugit soluta quo esse quos beatae neque, sapiente inventore. Saepe distinctio earum at." 
    },
    {
        "slug":"car loans",
        "image":"birinci.png",
        "date":date(2023, 5, 23),
        "title": "Idunno2",
        "excerpt": "What is happening!2",
        "content":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure, eos rem amet culpa harum repudiandae quae quam fugit soluta quo esse quos beatae neque, sapiente inventore. Saepe distinctio earum at." 
    },
    {
        "slug":"business lines of credit",
        "image":"birinci.png",
        "date":date(2023, 8, 23),
        "title": "Idunno3",
        "excerpt": "What is happening!3",
        "content":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure, eos rem amet culpa harum repudiandae quae quam fugit soluta quo esse quos beatae neque, sapiente inventore. Saepe distinctio earum at." 
    }
]

def starting_page(request):
    return render(request, "credit/index.html")

def credits(request):
    return render(request, "credit/all-credits.html")

def credit_detail(request,slug):
    return render(request,"credit/credit-detail.html")