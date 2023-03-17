from django.contrib import admin
from .models import Credit,Customer,Address,BankOption, Application

# Register your models here.

class CreditAdmin(admin.ModelAdmin): # this class allows you to set various options and fields that will be reflected in the admin page
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("name","interest_rate","loan_amount")
    list_display = ("name","loan_amount")

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("full_name",)

class BankOptionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",),}

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("identification_number","bank_name","credit_name")

admin.site.register(Credit,CreditAdmin) 
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Address)
admin.site.register(BankOption,BankOptionAdmin)
admin.site.register(Application,ApplicationAdmin)
#tells django this model should be added to the administration site