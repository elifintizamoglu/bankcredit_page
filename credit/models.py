from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=30,null=True)
    district = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=5,null=True)

    def __str__(self):
        return f"{self.street}, {self.district}, {self.city}, Postal Code: {self.postal_code} "
    
    class Meta: #register special settings, which will affect how this model is used
        verbose_name_plural = "Address Entries" #how to address model is outputted when plural needed


class Customer(models.Model):
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100,null=False)
    identification_number = models.CharField(null=False,unique=True,max_length=11)
    job_title = models.CharField(max_length=50,null=True)
    salary = models.IntegerField(validators=[MinValueValidator(10000)],null=True)
    address = models.ForeignKey(Address,on_delete=models.SET_NULL,null=True)

    def full_name(self):
        return f"{self.first_name}  {self.last_name}"

    def __str__(self):
        return self.full_name()
    

class Credit(models.Model):
    name = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=150)
    content = models.TextField(validators=[MinLengthValidator(10)])
    image_name = models.CharField(max_length=30,null=True)
    slug = models.SlugField(default="",null=False,db_index=True,unique=True)
    loan_amount = models.IntegerField(default=500000,validators=[MinValueValidator(500000),MaxValueValidator(6000000)])
    interest_rate = models.DecimalField(max_digits=6,decimal_places=4)

    def __str__(self):
        return f"{self.name}"


class BankOption(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(default="",null=False,db_index=True,unique=True)
    credit_types = models.ManyToManyField(Credit)

    def __str__(self):
        return f"{self.name}"
    
    """
    def get_absolute_url(self):
        return reverse('bank:credit_detail', kwargs={"bank": self.slug, "credit": self.credit_types.slug})
    """