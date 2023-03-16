from django import forms
from .models import Customer,Address

"""
class ApplicationForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields = '__all__'
"""   


class ApplicationForm(forms.Form):
    first_name=forms.CharField(max_length=100, error_messages={"required":"Your first name must not be empty!", "max_length":"Enter a shorter first name!"
    })
    last_name = forms.CharField(max_length=100, error_messages={"required":"Your last name must not be empty!", "max_length":"Enter a shorter last name!"
    })
    identification_number= forms.CharField(max_length=11,min_length=11,error_messages={"unique":"This identification number has been already registered!"})
    job_title = forms.CharField(max_length=50)
    salary = forms.IntegerField()
    district = forms.CharField(max_length=30)
    city = forms.CharField(max_length=30)



