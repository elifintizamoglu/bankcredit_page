from django.contrib import admin
from .models import Credit

# Register your models here.

class CreditAdmin(admin.ModelAdmin): # this class allows you to set various options and fields that will be reflected in the admin page
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("name","interest_rate","loan_amount")
    list_display = ("name","loan_amount")

admin.site.register(Credit,CreditAdmin) #tells django this model should be added to the administration site