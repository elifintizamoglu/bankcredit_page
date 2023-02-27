from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Credit(models.Model):
    name = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=150)
    content = models.CharField(max_length=500)
    slug = models.CharField(max_length=80,default="credittype" )
    interest_rate = models.DecimalField(max_digits=6,decimal_places=4)
    loan_amount = models.IntegerField(default=500000,validators=[MinValueValidator(500000),MaxValueValidator(6000000)])
    
    def __str__(self): #whenever it is outputed, that is how it should be converted
        return f"{self.name}"
