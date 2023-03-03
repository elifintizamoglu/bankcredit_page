from django import forms

class ApplicationForm(forms.Form):
    first_name=forms.CharField(max_length=100, error_messages={"required":"Your first name must not be empty!", "max_length":"Enter a shorter first name!"
    })
    last_name = forms.CharField(max_length=100, error_messages={"required":"Your last name must not be empty!", "max_length":"Enter a shorter last name!"
    })
    identification_number= forms.IntegerField(min_value=11111111111, max_value= 99999999999)
    job_title = forms.CharField(max_length=50)
    salary = forms.IntegerField(min_value=10000)
    street = forms.CharField(max_length=30)
    building_name= forms.CharField(max_length=30)
    flat_no = forms.IntegerField(min_value=0, max_value= 999)
    district = forms.CharField(max_length=30)
    city = forms.CharField(max_length=30)
    postal_code = forms.CharField(max_length=5)