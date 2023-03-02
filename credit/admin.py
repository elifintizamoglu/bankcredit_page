from django.contrib import admin
from .models import Credit,Customer,Address

# Register your models here.

class CreditAdmin(admin.ModelAdmin): # this class allows you to set various options and fields that will be reflected in the admin page
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("name","interest_rate","loan_amount")
    list_display = ("name","loan_amount")

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("full_name",)


admin.site.register(Credit,CreditAdmin) 
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Address)
#tells django this model should be added to the administration site